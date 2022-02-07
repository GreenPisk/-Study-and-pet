#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float64
import math,time

class PID():

    def __init__(self, Kp = 0, Ki = 0, Kd = 0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.Result_I = 0
        self.previous_error = 0


    def PID_R(self, error):
        self.error = error
        Result_P = self.Kp * self.error
        self.Result_I += self.Ki * self.error
        Result_D = self.Kd * (self.error - self.previous_error)
        self.previos_error = self.error
        self.Result_PID = Result_P +   self.Result_I + Result_D
        return(self.Result_PID)


class TurtleBot:
    TIME_FOR_SIDE = rospy.Duration(3)
    TURN_ANGLE = math.radians(90)


    def __init__(self):
        rospy.init_node('Turtle_p', anonymous = True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        self.Pose = rospy.Subscriber("turtle1/pose", Pose, self.update_pose)

        self.command = Twist()
        self.command.linear.x = 1
        self.PID = PID(20, 1.0, 0.0)
        self.current_angle = 0
        self.rate = rospy.Rate(20)


    def update_pose(self,data):
        self.current_angle = data.theta


    def angle_difference(self, sourceA, targetA):
        a = targetA - sourceA
        a = (a + math.radians(180)) % math.radians(360) - math.radians(180)
        return a


    def loop(self):
        time = rospy.get_rostime()
        Angle = 0
        while not rospy.is_shutdown():
            if rospy.get_rostime() > time + self.TIME_FOR_SIDE:
                time = rospy.get_rostime()
                Angle += self.TURN_ANGLE
            error = self.angle_difference(self.current_angle, Angle)
            self.command.angular.z = self.PID.PID_R(error)
            self.velocity_publisher.publish(self.command)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.loop()
    except rospy.ROSInterruptException:
        pass

