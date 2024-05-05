'''
This script sets up & trains the Sawyer robot the optimal ball striking stroke using a
Twin Delayed Deep Deterministic (TD3) RL architecture to train our ping pong robot. It
follows the approach proposed in the Optimal Stroke Learning with Policy Gradient Approach
for Robotic Table Tennis.

How it Works:
1) Initially sets up the actor & critic neural networks
2) Sets up the replay buffer to store experiences? Randomly sampled when calculating loss function
and performing gradient descent (to eliminate temporal bias/correlation which would make model
worse)
3) Sets up OpenAI gym, state/action dimensionality, actor/critic/optimizer objects, learning &
discount coefficients, episode & batch sizes, etc
4) Contains training loop
In each episode,
----> Resets the OpenAI gym environment at beginning
----> For each step, it calculates the action, states, next actions, next states, & reward in
that timestep (as well as reward overall to evaluate the episode), which serve as inputs to
the actor & critic loss functions, respectively.
----> Additionally, in each time step, we calculate two Q-values (following the TD3 approach),
and take the minimum of two for stability (also following the TD3 approach)
----> These Q-values are then combined with their (weighted) future reward (which is found with
 the next states/actions) to calculate a final Q-value
 ---> This final Q-value is then fed into the less functions & used to perform gradient descent
 & backpropagate/update the weights/biases on our actor & critic(s) neural networks.

Considerations: #TODO
- How to account for not hitting the table
- How to make sure the paddle never spawns inside of the Sawyer robot.... (non-RL)
- Creating OpenAI gym representation/set up framework with Gazebo/ROS
----> Returns some sort of "done" value (0-1) representing completion or lack thereof of the
episode (i.e. likely ball falling off table eventually), returns some reward (likely just how
far we are in that time step(?) from target, and of course, our current states/actions/next
actions, which are integral to it all.
'''

import gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random

class Actor(nn.Module):
    # Initializes the actor (and its network)
    def __init__(self, state_dim, action_dim, max_action):
        """
        Initialize the Actor network.

        Parameters:
        - state_dim (int): Dimension of the state space.
        - action_dim (int): Dimension of the action space.
        - max_action (float): Scaling factor for output actions.

        Returns:
        None
        """
        super(Actor, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim),
            nn.Tanh()   # Assumes action values need to be betweenn -1 and 1 #TODO: Fix as needed
        )
        self.max_action = max_action #TODO: Fix as needed

    def forward(self, state):
        """
        Forward pass through the Actor network.

        Parameters:
        - state (torch.Tensor): Input state tensor.

        Returns:
        - torch.Tensor: Scaled action values in the range [-max_action, max_action].
        """
        return self.max_action * self.network(state) #TODO: Fix as needed

class Critic(nn.Module):
    def __init__(self):
        """
        Initialize the Critic networks.

        Parameters:
        - state_dim (int): Dimension of the state space.
        - action_dim (int): Dimension of the action space.

        Returns:
        None
        """
        super(Critic, self).__init__()
        self.q_net1 = self.build_network(state_dim, action_dim)
        self.q_net2 = self.build_network(state_dim, action_dim)

    def build_network(self, state_dim, action_dim):
        """
        Build a neural network for the Critic.

        Parameters:
        - state_dim (int): Dimension of the state space.
        - action_dim (int): Dimension of the action space.

        Returns:
        - torch.nn.Sequential: Critic network.
        """
        return nn.Sequential(
            nn.Linear(state_dim + action_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim) # 3D Q-value: [Qx, Qy, Qh] #TODO: how does this actually end up being effective?
        )

    def Q1(self, state, action):
        """
        Compute the Q-value using the first critic network.

        Parameters:
        - state (torch.Tensor): Input state tensor.
        - action (torch.Tensor): Input action tensor.

        Returns:
        - torch.Tensor: Q-value from the first critic network.
        """
        states_actions = torch.cat([state, action], dim=1)
        return self.q_net1(states_actions)

    def forward(self, state, action):
        """
        Compute the Q-values using both critic networks.

        Parameters:
        - state (torch.Tensor): Input state tensor.
        - action (torch.Tensor): Input action tensor.

        Returns:
        - (torch.Tensor, torch.Tensor): Q-values from both critic networks.
        """
        states_actions = torch.cat([state, action], dim=1)
        return self.q_net1(states_actions), self.q_net2(states_actions)

class ReplayBuffer:
    def __init__(self, max_size):
        """
        Initialize the replay buffer.

        Parameters:
        - max_size (int): Maximum size of the replay buffer.

        Returns:
        None
        """
        self.buffer = []
        self.max_size = max_size
        self.size = 0

    def add(self, entry):
        """
        Add an entry to the replay buffer.

        Parameters:
        - entry (tuple): Tuple containing (state, action, reward, next_state, done).

        Returns:
        None
        """
        self.buffer.append(entry)
        self.size += 1
        if self.size > self.max_size:
            self.buffer.pop(0)
            self.size -= 1

    def sample(self, batch_size):
        """
        Sample a batch of experiences from the replay buffer.

        Parameters:
        - batch_size (int): Number of experiences to sample.

        Returns:
        - (np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray): Tuple containing arrays of states, actions, rewards, next_states, and dones.
        """
        index = np.random.choice(np.arange(self.size), size=batch_size, replace=False)
        states, actions, rewards, next_states, dones = zip(*[self.buffer[i] for i in index])
        return np.array(states), np.array(actions), np.array(rewards), np.array(next_states), np.array(dones)

class TableTennisEnv(gym.Env):
    #TODO: This gives a very basic outline
    def __init__(self):
        """
        Initialize the Table Tennis environment.

        Returns:
        None
        """
        # Initializes the Table Tennis environment
        super(TableTennisEnv, self).__init__()
        #TODO: Probably account for the different bounds of the different attributes (e.g. position, velocities, etc) in the observation/action space
        self.observation_space = gym.spaces.Box(low=-10, high=10, shape=(11,), dtype=np.float32) # 11-dimensional vector of position, linear/angular velocities, & target
        self.action_space = gym.spaces.Box(low=-10, high=10, shape=(3,), dtype=np.float32) # TODO: change (paper uses lin vel x & angling of paddle wrt y & z)
        self.state = None

    def reset(self):
        """
        Reset the environment to the initial state.

        Returns:
        - np.ndarray: Initial state of the environment.
        """
        #TODO: reset the environment to have no ball, then spawn w/ random valid position & velocity
        #TODO: The following is a placeholder (MUST be replaced)
        self.state = np.random.uniform(-10, 10, size=(11,))
        return self.state

    def step(self, action):
        """
        Apply an action to the environment and obtain the next state, reward, and done flag.

        Parameters:
        - action (np.ndarray): Action to be applied.

        Returns:
        - (np.ndarray, np.ndarray, bool, dict): Tuple containing the next state, reward, done flag, and additional info.
        """
        #TODO: Completely replace the following
        # Update state based on the action
        next_state = self.state + action  # Simplified for illustration purposes (use the actor, something with argmax of action that maximizes q-value)
        # Reward is a random 3D vector here; replace with real implementation
        reward = np.random.random(3) # Do the e^__ as shown in the Reward Shaping section
        done = np.random.random() < 0.1  # Terminated when height falls below specific threshold; This is a Random termination condition for demonstration
        self.state = next_state
        return next_state, reward, done, {}

    def render(self, mode='human'):
        pass

    def close(self):
        """
        Clean up resources used by the environment.

        Returns:
        None
        """
        #TODO
        pass

# Training Loop
def train(num_episodes=10000, batch_size=64, gamma=0.99, lr_both=1e-4, max_action=1.0, action_noise=0.1, noise_clip=0.5, policy_delay=2):
    """
    Train the Sawyer robot using the TD3 architecture.

    Parameters:
    - num_episodes (int): Number of training episodes.
    - batch_size (int): Size of the training batch.
    - gamma (float): Discount factor.
    - lr_both (float): Learning rate for both actor and critic.
    - max_action (float): Scaling factor for output actions.
    - action_noise (float): Standard deviation of noise to add to actions for exploration.
    - noise_clip (float): Clip value for action noise.
    - policy_delay (int): Frequency of policy updates relative to critic updates.

    Returns:
    None
    """
    # Initialize the environment, actor, and critic
    env = TableTennisEnv()
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]
    actor = Actor(state_dim, action_dim, max_action)
    critic = Critic(state_dim, action_dim)
    actor_optimizer = optim.Adam(actor.parameters(), lr=lr_both)
    critic_optimizer = optim.Adam(critic.parameters(), lr=lr_both)
    replay_buffer = ReplayBuffer(5000)

    for episode in range(num_episodes):
        state = env.reset()
        total_reward = np.zeros(3)  # Multidimensional reward
        done = False
        step = 0

        while not done:
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            action = actor(state_tensor).detach().cpu().numpy()[0]
            action = action.clip(env.action_space.low, env.action_space.high)

            next_state, reward, done, _ = env.step(action)
            total_reward += reward
            replay_buffer.add((state, action, reward, next_state, done))
            state = next_state
            step += 1

            if len(replay_buffer.buffer) > batch_size:
                states, actions, rewards, next_states, dones = replay_buffer.sample(batch_size)
                states = torch.FloatTensor(states)
                actions = torch.FloatTensor(actions)
                rewards = torch.FloatTensor(rewards)
                next_states = torch.FloatTensor(next_states)
                dones = torch.FloatTensor(dones)

                # Compute target Q values for the next state
                with torch.no_grad():
                    noise = torch.FloatTensor(actions).data.normal_(0, action_noise).clip(-noise_clip, noise_clip)
                    next_actions = (actor(next_states) + noise).clip(env.action_space.low, env.action_space.high)
                    next_Q1, next_Q2 = critic(next_states, next_actions)
                    min_next_Q = torch.min(next_Q1, next_Q2, dim=1)[0]
                    target_Q = rewards + gamma * (1 - dones) * min_next_Q

                current_Q1, current_Q2 = critic(states, actions)

                # Compute critic loss
                critic_loss = torch.nn.functional.mse_loss(current_Q1, target_Q) + \
                              torch.nn.functional.mse_loss(current_Q2, target_Q)

                # Critic gradient descent
                critic_optimizer.zero_grad()
                critic_loss.backward()
                critic_optimizer.step()

                # Delayed updates for actor network (TD3 backbone feature)
                if step % policy_delay == 0:
                    actor_loss = -critic.Q1(states, actor(states)).mean()
                    actor_optimizer.zero_grad()
                    actor_loss.backward()
                    actor_optimizer.step()

        print(f"Episode: {episode + 1}, Total Reward: {total_reward}")
    env.close()

# Execute Training
if __name__ == "__main__":
    train()