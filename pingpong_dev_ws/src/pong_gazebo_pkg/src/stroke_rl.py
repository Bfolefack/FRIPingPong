'''
This script sets up & trains the sawyer robot the optimal ball striking stroke using a
Twin Delayed Deep Deterministic (TD3) RL architecture to train our ping pong robot. It
follows the approach proposed in the Optimal Stroke Learning with Policy Gradient Approach
for Robotic Table Tennis.

How it Works:
1) Initially sets up the actor & critic neural networks
2) Sets up the replay buffer to store experiences? #TODO
3) Sets up OpenAI gym, state/action dimensionality, actor/critic/optimizer objects, learning &
discount coefficients, episode & batch sizes, etc
4) Contains training loop
---->
---->

Considerations:
- How to account for not hitting the table
- How to make sure the paddle never spawns inside of the Sawyer robot....
'''
