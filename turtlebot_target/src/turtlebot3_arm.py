import roslib; roslib.load_manifest('my_simulations')
import rospy
from std_msgs.msg import Float64
import math

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

def arm():
    pub = rospy.Publisher('/joint1_position_controller/command', Float64 ,queue_size=10)
    rospy.init_node('turtlebot3_arm')
    rate = rospy.Rate(10) # 50hz
    while not rospy.is_shutdown():    
        position = -math.pi/2
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
        

if __name__== '__main__':
    try:
        arm()

    except rospy.ROSInterruptException:
        pass