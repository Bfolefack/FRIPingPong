#! /usr/bin/env python
import traceback
import rospy
import sys
import rospy
import moveit_commander
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header
import tf2_ros
import tf2_geometry_msgs
from sensor_msgs.msg import JointState

import numpy as np 

WORLD_FRAME = "base"
EE_FRAME = "right_gripper_tip"
GROUP_NAME = "sawyer_arm"

class RightArm(object):
    def __init__(self):
        super(RightArm, self).__init__()

        # initialize moveit 
        moveit_commander.roscpp_initialize(sys.argv)
        self.group = MoveGroupCommander(GROUP_NAME)

        # Setup a transform buffer to swap poses between frames
        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)



    def translate_in_ee_frame(self, distance):
        """
        Move the end-effector by @distance in the local frame of the end-effector. 
        @distance: np.array shape (3,)
        """
        # TODO: Create a PoseStamped message, @distance w.r.t the EE_FRAME
        # hint: use the following message types:
        # - Header(frame_id = ?)
        # - Point(x, y, z)
        # - Quaternion(x, y, z, w)
        # - Pose(position, rotation)
        # - PoseStamped(header, pose)
        msg = PoseStamped(Header(), Pose())
        msg.header.frame_id = EE_FRAME
        msg.header.stamp = rospy.Time.now()
        msg.header.stamp.secs += 1
        msg.pose.position = Point(distance[0], distance[1], distance[2])
        msg.pose.orientation = Quaternion(0, 0, 0, 1)
        


    
        # TODO: Transform the pose to WORLD_FRAME
        # hint: use self.tf_buffer.transform
        try:
            if(self.tf_buffer.can_transform(WORLD_FRAME, EE_FRAME, rospy.Time(0,0), rospy.Duration(1.0))):
                pose_in_world = self.tf_buffer.transform(object_stamped=msg, target_frame="base", timeout=rospy.Duration(1.0))
                print("Pose successfully transformed")
                print()
                print("Target pose:")
                print(pose_in_world)
                print()
                print()
                # TODO: Set the pose as target and go
                # hint: use self.group: self.group.set_pose_target and self.group.go 
                self.group.set_pose_target(pose_in_world)
                self.group.go()
                print("Moved")
            else:
                print("Cannot transform")
            
        except (Exception):
            print("Unknown error transforming pose")
            traceback.print_exc()
            return

        
        return
    



arm = None

def joint_state_callback(data: JointState):
    print("Joint state callback")
    print(data)
    return

if __name__ == '__main__':

    # initialize node
    rospy.init_node('pingpong_moveit')

    # create RightArm object
    arm = RightArm()
    # planning_frame = arm.group.get_planning_frame()
    # print("Planning frame: ", planning_frame)
    # eef_link = arm.group.get_end_effector_link()
    # print("End effector link: ", eef_link)
    # group_names = moveit_commander.RobotCommander().get_group_names()
    # print("Group names: ", group_names)
    # current_state = moveit_commander.RobotCommander().get_current_state()
    # print("Current state: ", current_state)
    # all_frames_str = arm.tf_buffer.all_frames_as_string()
    # print("All frames: ", all_frames_str)
    
    # TODO: form a vector representing 5cm in the x-direction
    # this should be a numpy array of shape (3,)
    print()
    print("Current pose:\n", arm.group.get_current_pose())
    print()
    print()
    
    # joint_states_listener = rospy.Subscriber("/joint_states", JointState, joint_state_callback)
    
    displacement = np.array([0.0,0.0, -0.1465])

    arm.translate_in_ee_frame(displacement)