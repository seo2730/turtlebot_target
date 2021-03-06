#!/usr/bin/env python
# license removed for brevity
import roslib; roslib.load_manifest('turtlebot_target')
import rospy
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# Map subscribe
from nav_msgs.msg import OccupancyGrid

from std_msgs.msg import UInt8

import time

# Keyboard in Linux
import sys
import tty
import termios

def getKey():
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return ch

def movebase_client(x,y,z):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = 1.0

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

def arm(a):
    arm = a
    pub.publish(arm)
    
# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    rospy.init_node('moving_serving')
    pub = rospy.Publisher('serving', UInt8 ,queue_size=10)

    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        while not rospy.is_shutdown():
            key = getKey()
            if key == 'q':
                arm(1)
                print("Go to Q place")
                movebase_client(2.5,1.5,1.0)
                # robot arm #
                print("Setting a pizza")
                arm(0)
                movebase_client(0.0,0.0,0.0)
            
            elif key == 'w':
                arm(1)
                print("Go to W place")
                movebase_client(1.5,2.5,-1.0)
                # robot arm #
                print("Setting a pizza")
                arm(0)
                movebase_client(0.0,0.0,0.0)

            elif key == 'e':
                arm(1)
                print("Go to E place")
                movebase_client(2.0,0.0,0.0)
                # robot arm #
                print("Setting a pizza")
                arm(0)
                movebase_client(0.0,0.0,0.0)
            
            
        
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")


    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
