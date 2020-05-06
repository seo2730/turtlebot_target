# turtlebot_target
Make turtlebot go to the target using keyboard

# Import
 rospy : You have to import rospy to use ros<br>
 actionlib : 
 
    import rospy
    import actionlib
    from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
    from nav_msgs.msg import OccupancyGrid
