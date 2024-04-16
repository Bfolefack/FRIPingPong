#!/usr/bin/env python3
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image
import rospy
import image_view


color_image_received = False
depth_image_received = False


def get_ball_image_position(self, image: Image):
    return (0.5, 0.5)



def image_callback(msg: Image):
    print("Color Image received")
    image_view.imshow(msg)
    pass
def depth_callback(msg: Image):
    print("Depth Image received")
    pass
    
def launch_ball_tracker():
    color_image = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
    depth_data = rospy.Subscriber("/camera/depth/image_raw", Image, depth_callback)
    image1_ball_pos = [-1.0, -1.0]
    image2_ball_pos = [-1.0, -1.0]

    ball_position = Vector3()
    ball_position.x = 0
    ball_position.y = 0
    ball_position.z = 0

    rospy.init_node('ball_tracker')
    ball_position_pub = rospy.Publisher('/ball_position', Vector3, queue_size=10)

launch_ball_tracker()
rospy.spin()