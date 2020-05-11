# turtlebot_target
Make turtlebot go to the target using keyboard

# Import for turtlebot
 rospy : You have to import rospy to use ros<br>
 actionlib : ros package to action<br>
 move_base_msgs, nav_msgs : message file<br>
 MoveBaseAction, MoveBaseGoal : move_base for action & goal<br>
 OccupancyGrid : cartestian coordinate(might be???)<br>
 
    import rospy
    import actionlib
    from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
    from nav_msgs.msg import OccupancyGrid

# Import for Keyboard in Linux

    import sys
    import tty
    import termios
    
# Keyboard Code 

    def getKey():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch
        
# Target & Navigation Code
movebase_client(x,y,z)<br>
: x,y is turtlebot coordinate, z is turtlebot direction<br>

move_base is rosservice. Not rostopic
 
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
