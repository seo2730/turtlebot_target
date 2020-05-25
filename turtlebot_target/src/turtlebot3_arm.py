#!/usr/bin/env python
# license removed for brevity
import roslib; roslib.load_manifest('my_simulations')
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import UInt8
import math

# Keyboard in Linux
import sys
import tty
import termios

ser = 0

def arm_callback(m):
    global ser
    ser = m.data
    if ser == 0:
        arm(-0.9,-0.9,0.9,0.9)

    elif ser == 1:
        arm(0.0,0.0,0.0,0.0)

def arm_listener():
    rospy.Subscriber("serving", UInt8, arm_callback)
    rospy.spin()


def arm(joint1, joint2, joint3, joint4):   
    position1 = joint1
    position2 = joint2
    position3 = joint3
    position4 = joint4

    pub1.publish(position1)
    pub2.publish(position2)
    pub3.publish(position3)
    pub4.publish(position4)
    rate.sleep()
        

if __name__== '__main__': 
    rospy.init_node('turtlebot3_arm', anonymous=True)

    pub1 = rospy.Publisher('/joint1_position_controller/command', Float64 ,queue_size=10)
    pub2 = rospy.Publisher('/joint2_position_controller/command', Float64 ,queue_size=10)
    pub3 = rospy.Publisher('/joint3_position_controller/command', Float64 ,queue_size=10)
    pub4 = rospy.Publisher('/joint4_position_controller/command', Float64 ,queue_size=10)

    rate = rospy.Rate(50) # 50hz 

    try:
        arm_listener()


    except rospy.ROSInterruptException:
        rospy.loginfo("Arm deactivated.")
    finally:
        arm(0.0,0.0,0.0,0.0)

    if ox.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)