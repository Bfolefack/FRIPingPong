#!/usr/bin/env python3
from gazebo_msgs.msg import LinkStates
from geometry_msgs.msg import Vector3
import rospy


ball_position_pub = rospy.Publisher('/ball_position', Vector3, queue_size=10)

def model_states_callback(msg: LinkStates):
    print("Model States received")
    for i in range(len(msg.name)):
        if(msg.name[i] == "pong_system::ball_link"):
            print(msg.name[i])
            print(msg.pose[i].position)
            print()
            print()
            
    ball_index = msg.name.index("pong_system::ball_link")
    ball_position = msg.pose[ball_index].position
    ball_position_msg = Vector3()
    ball_position_msg.x = ball_position.x
    ball_position_msg.y = ball_position.y
    ball_position_msg.z = ball_position.z
    ball_position_pub.publish(ball_position_msg)
    pass

model_states_sub = rospy.Subscriber('/gazebo/link_states', LinkStates, model_states_callback)

def launch_ball_coupler():
    rospy.init_node('ball_coupler')
    rospy.spin()
    pass

launch_ball_coupler()