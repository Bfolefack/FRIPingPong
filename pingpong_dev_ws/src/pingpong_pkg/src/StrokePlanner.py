import rospy
from BallTrajectoryPlanner import BallState
from geometry_msgs.msg import Vector3

class Stroke :
    def __init__(self):
        self.velocity = Vector3()
        self.orientation = Vector3()

def ball_state_callback(msg: BallState):
    pass

ball_state_sub = rospy.Subscriber('/ball_state', BallState, ball_state_callback)
stroke_pub = rospy.Publisher('/stroke', Stroke, queue_size=10)

rospy.init_node('stroke_planner')
rospy.spin()