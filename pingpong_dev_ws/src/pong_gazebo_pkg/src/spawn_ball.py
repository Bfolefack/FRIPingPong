#!/usr/bin/env python

'''
The following script will spawn in a ping pong ball
with variable position & orientation (so that it hits
the ping pong table).

This will be used when training the RL model that will
teach the sawyer robot the optimal stroke path/trajectory.
'''

import rospy, rospkg, os, random, re

from gazebo_msgs.msg import *
from gazebo_msgs.srv import *

from gazebo_ros import gazebo_interface
from geometry_msgs.msg import Pose, Quaternion


class SpawnModel:
    def __init__(self):

        # Member Variables
        self.model_name = 'ping_pong_ball'
        self.robot_namespace = rospy.get_namespace()
        self.reference_frame = 'world'          # Default value
        self.gazebo_namespace = '/gazebo'      # Default value
        self.readyToSpawn = True
        self.ballExists = False
        self.ballDropHeightThreshold = 0.15
        self.ballBelowThreshold = False

    '''
    Spawns in the ball with the desired velocity.

    NOTE: For use, you should pass in randomized valid ball vel 
    to ensure that the trained ping pong playing sawyer robot 
    model is robust.
    
    NOTE: This will always start shooting the ball from the same
    position; with different velocities, though, the ball can land
    almost anywhere on the robot's side of the table.

    Params
    ----------------
    self:
    vel: list [vx, vy, vz, wx, wy, wz]
        Velocity list (both linear & angular) for the spawned ball

    Returns 
    ----------------

    '''
    def ballSpawner(self, vel):
        if self.readyToSpawn and not self.ballExists:
            rospy.loginfo("Successfully got ready to spawn the ball")
            # Gets an instance of RosPack, which has the associated ROS search paths
            rospack = rospkg.RosPack()

            # Get relative path of the pong_gazebo_pkg
            pong_gazebo_pkg_file_path = rospack.get_path('pong_gazebo_pkg')

            # Get filepath of urdf of ball
            ball_urdf_file_path = pong_gazebo_pkg_file_path + '/models/ball/ball.urdf'

            # Copies the contents of the ball urdf file into ball_model_xml
            with open(ball_urdf_file_path, 'r') as ball_urdf_file:
                ball_model_xml = ball_urdf_file.read()

            initial_ball_pose = Pose()
            initial_ball_pose.position.x = 3#3.4932 #TODO
            initial_ball_pose.position.y = 0.0#-1.00 #TODO
            initial_ball_pose.position.z = 2 #TODO
            # The quaternion is simply the identity quaterion (since it doesn't really matter)
            initial_ball_pose.orientation = Quaternion(1, 0, 0, 0)

            ball_model_xml = self.setVelocity(ball_model_xml, vel)

            # The arguments for gazebo_interface.spawn_urdf_model which aren't define in this ballSpawner class are instance variables defined in constructor
            success = gazebo_interface.spawn_urdf_model_client(self.model_name, ball_model_xml, self.robot_namespace, initial_ball_pose, self.reference_frame, self.gazebo_namespace)

            rospy.loginfo("Successfully spawned the ball")
            self.readyToSpawn = False
            self.ballExists = True

            return
        rospy.loginfo("Ball was not spawned")

    def deleteService(self):
        if(self.ballExists and self.ballBelowThreshold):
            try:
                # Creates a service (whose name is the first parameter) that calls the gazebo_msgs.srv DeleteModel service
                delete_model = rospy.ServiceProxy('%s/delete_model' % self.gazebo_namespace, DeleteModel)
                # Deletes the model
                delete_model(model_name=self.model_name)
                self.readyToSpawn = True
                rospy.loginfo("Ball has been deleted")
                return
            except rospy.ServiceException as e:
                # May be induced bc there is nothing to delete or the delete failed (likely the latter)
                rospy.logerr("Delete model service call failed: {}".format(e))
        rospy.loginfo("Nothing was deleted")

    '''
    Sets the velocity of the ball urdf xml by substituting
    in the velocity arguments
    
    Params:
    ------------------
    self:
    ball_model_xml: xml
        The urdf xml for the ball to be spawned
    velocity: list [vx, vy, vz, wx, wy, wz]
        Velocity list (both linear & angular) for the spawned ball 
    
    Returns:
    ------------------ 
    ball_model_xml: xml
        The UPDATED urdf xml for the ball to be spawned 
    '''
    def setVelocity(self, ball_model_xml, vel):
        print('vel: ', vel)

        lin_vel_x = str(vel[0])
        lin_vel_y = str(vel[1])
        lin_vel_z = str(vel[2])
        ang_vel_x = str(vel[3])
        ang_vel_y = str(vel[4])
        ang_vel_z = str(vel[5])
        ball_model_xml = re.sub("<linear>.*<\/linear>", "<linear>{0} {1} {2}<\/linear>".format(lin_vel_x, lin_vel_y, lin_vel_z), ball_model_xml)
        ball_model_xml = re.sub("<angular>.*<\/angular", "<angular>{0} {1} {2}<\/angular>".format(ang_vel_x, ang_vel_y, ang_vel_z), ball_model_xml)
        rospy.loginfo("setVelocity() function called")
        return ball_model_xml

    def deleteServiceFinal(self):
        if(self.ballExists):
            try:
                # Creates a service (whose name is the first parameter) that calls the gazebo_msgs.srv DeleteModel service
                delete_model = rospy.ServiceProxy('%s/delete_model' % self.gazebo_namespace, DeleteModel)
                # Deletes the model
                delete_model(model_name=self.model_name)
                self.readyToSpawn = True
                rospy.loginfo("Final deletion")
            except rospy.ServiceException as e:
                # May be induced bc there is nothing to delete or the delete failed (likely the latter)
                rospy.logerr("Delete model service call failed: {}".format(e))
        rospy.loginfo("deleteServiceFinal() function called")


    '''
    Generates a random ball velocity that will guaranteed
    land on the robot's side of the table.
    
    Params:
    ------------------
    self:
    
    Returns:
    ------------------ 
    velocity: list [vx, vy, vz, wx, wy, wz]
        Velocity list (both linear & angular) for the spawned ball 
    '''
    def randomBallVel(self):
        # TODO: add functionality to randomize the velocity of the ball
        velocity = [-1, 0, 0, 0, 0, 0]
        rospy.loginfo("Generated 'random' ball velocity")
        return velocity

    '''
    Checks whether the ball model exists amongst the list of current
    models in Gazebo
    
    Params:
    ------------------
    self:
        model_states: gazebo_msgs/ModelStates.msg
            ModelStates message from gazebo_msgs, which contains:
                string[] name                 # model names
                geometry_msgs/Pose[] pose     # desired pose in world frame
                geometry_msgs/Twist[] twist   # desired twist in world frame     
    
    Returns:
    ------------------ 
    ballExists: bool 
        Boolean stating whether the ball model exists (true) or doesn't (false)
    '''
    def checkForModel(self, model_states):
        for n in model_states.name:
            if n == 'ping_pong_ball':
                self.ballExists = True
                self.checkDropBelowThreshold(model_states)
                return
        self.ballExists = False
        # rospy.loginfo("checkForModel() function called")


    '''
    Checks whether the ball model has fallen below the threshold (and thus off 
    the table)
    
    NOTE: This ONLY works if the ball exists (which should be covered by the 
    check first regarding whether the ball exists where this is called
    
    Params:
    ------------------
    self:
        model_states: gazebo_msgs/ModelStates.msg
            ModelStates message from gazebo_msgs, which contains:
                string[] name                 # model names
                geometry_msgs/Pose[] pose     # desired pose in world frame
                geometry_msgs/Twist[] twist   # desired twist in world frame     
    
    Returns:
    ------------------ 
    
    '''
    def checkDropBelowThreshold(self, model_states):
        try:
            i = 0
            for n in model_states.name:
                if n == 'ping_pong_ball':
                    if(model_states.pose[i].position.z <= self.ballDropHeightThreshold):
                        self.ballBelowThreshold = True
                        rospy.loginfo("Ball has dropped below threshold: {}".format(model_states.pose[i].position.z))
                        return
                    else:
                        self.ballBelowThreshold = False
                        rospy.loginfo("Ball has not yet dropped below threshold: {}".format(model_states.pose[i].position.z))
                        return
                i += 1
            rospy.loginfo("Checked whether ball dropped below threshold")
            raise ValueError("There is no ball, so there is no drop threshold to check")
        except Exception as e:
            rospy.logerr("Encountered an error: {}".format(e))


# class ModelChecker():
#     def __init__(self):
#         ballExists = False


if __name__ == "__main__":
    rospy.init_node('ball_model_spawner')
    spawnModel = SpawnModel()

    while not rospy.is_shutdown():
        # Conditions for spawn: first time, below certain height threshold (say 0.15, more than enough bc ball has diameter 0.04m)
        # -----> perhaps just check for certain height threshold & if error, do stuff anyway bc means it doesn't exist?
        # if()
        # Deletes any previously spawned models with the same name 'ping_pong_ball'

        rospy.Subscriber("%s/model_states"%(spawnModel.gazebo_namespace), ModelStates, spawnModel.checkForModel, queue_size=2, buff_size=2**24)

        spawnModel.deleteService()

        # Generates a random ball position & velocity that will land on the robot's side of the table
        velocity = spawnModel.randomBallVel()

        spawnModel.ballSpawner(velocity)
        # rospy.sleep(1)
    rospy.spin()
    rospy.on_shutdown(spawnModel.deleteServiceFinal) # Passing in deleteServiceFinal makes sure the existing ping_pong_ball model is deleted

    #####################################################################################################33333

    # def checkForModel(self, model):
    #     for n in model.name:
    #         if n == self.wait_for_model:
    #             self.wait_for_model_exists = True
    #
    # def callSpawnService(self, vel):
    #
    #     # wait for model to exist
    #     if not self.wait_for_model == "":
    #
    #         r= rospy.Rate(10)
    #         while not rospy.is_shutdown() and not self.wait_for_model_exists:
    #             r.sleep()

'''
# Intermediate function that is the callback for the rospy Subscriber
# which checks the current model states (list of models in Gazebo)
# 
# This function will create a ModelChecker object and then check for 
# the spawned ball
#     
# Params:
# ------------------
# self:
#     model_states: gazebo_msgs/ModelStates.msg
#         ModelStates message from gazebo_msgs, which contains:
#             string[] name                 # model names
#             geometry_msgs/Pose[] pose     # desired pose in world frame
#             geometry_msgs/Twist[] twist   # desired twist in world frame     
#     
# Returns:
# ------------------ 
# ballExists: bool 
#     Boolean stating whether the ball model exists (true) or doesn't (false)
# '''
# def intermediateCheckForModel(model_states):
#     model_checker = ModelChecker()
#     model_checker.checkForModel(model_states)


