from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image
import rospy


def get_ball_image_position(self, image: Image):
    return (0.5, 0.5)

def get_ball_position(self):
    #ball triangulation code here
    return self.ball_position

def image_callback(msg: Image):
        # ball image detection code here
        pass

image1_sub = rospy.Subscriber("/camera1/image_raw", Image, image_callback)
image2_sub = rospy.Subscriber("/camera2/image_raw", Image, image_callback)
image1_ball_pos = [-1.0, -1.0]
image2_ball_pos = [-1.0, -1.0]

ball_position = Vector3()
ball_position.x = 0
ball_position.y = 0
ball_position.z = 0

rospy.init_node('ball_tracker')
ball_position_pub = rospy.Publisher('/ball_position', Vector3, queue_size=10)
rospy.spin()
