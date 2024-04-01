from geometry_msgs.msg import Vector3
import rospy

ball_history: "list[Vector3]" = []

class BallState:
    def __init__(self):
        self.position = Vector3()
        self.velocity = Vector3()
        self.angular = Vector3()


#Math and physics stuff idk
def ball_position_callback(msg: Vector3):
    pass


ball_position_sub = rospy.Subscriber('/ball_position', Vector3, ball_position_callback)
ball_state_pub = rospy.Publisher('/ball_state', BallState, queue_size=10)

rospy.init_node('ball_trajectory_planner')
rospy.spin()