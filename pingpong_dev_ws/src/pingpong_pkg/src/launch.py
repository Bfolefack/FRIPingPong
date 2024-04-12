import roslaunch
import rospy
import atexit
from roslaunch.rlutil import get_or_generate_uuid
from roslaunch.parent import ROSLaunchParent
from BallTrajectoryPlanner import launch_trajectory_planner
from BallTracker import launch_ball_tracker
import pathlib
from pathlib import Path

mypath = pathlib.Path(__file__).parent.absolute()

rospy.init_node('en_Mapping', anonymous=True)
uuid = get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
#TODO: find a way to use relative path
rs2_camera_launch = ROSLaunchParent(uuid, [str(mypath) + "/launch/rs_camera.launch"])
rs2_camera_launch.start()
rospy.loginfo("\n\nstarted camera\n\n")

def onkill():
    rs2_camera_launch.shutdown()
    rospy.loginfo("\n\nkilled camera\n\n")
atexit.register(onkill)

launch_ball_tracker()
rospy.spin()