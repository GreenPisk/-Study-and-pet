#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float64
import math,time

class TurtleBot:
    Speed_Turtle = 3
    TURN_ANGLE = math.radians(90)

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        self.command = Twist()
        self.command.linear.x = self.Speed_Turtle
        self.ang = Twist()
        self.ang.angular.z = self.TURN_ANGLE


    def loop(self):
        self.rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            self.velocity_publisher.publish(self.command)
            self.rate.sleep()
            self.velocity_publisher.publish(self.ang)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.loop()
    except rospy.ROSInterruptException:
        pass
