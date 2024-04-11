from geometry_msgs.msg import Vector3
import rospy
from pingpong_pkg.msg import BallStateStamped

ball_history: "list[Vector3]" = []

#Math and physics stuff idk
def ball_position_callback(msg: Vector3):
    pass


ball_position_sub = rospy.Subscriber('/ball_position', Vector3, ball_position_callback)
ball_state_pub = rospy.Publisher('/ball_state', BallStateStamped, queue_size=10)

rospy.init_node('ball_trajectory_planner')
rospy.spin()