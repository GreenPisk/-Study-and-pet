import rospy
from geometry_msgs.msg import Twist
import math

def paramet_angl(angl):
    turn_angle = math.radians(angl)
    return turn_angle


def speed_paramet(vel, linvel=0, angvel=0):
    vel.linear.x = linvel
    vel.angular.z = angvel
    return vel


def move_tertle(line_vel,ang_vel):
    rospy.init_node('turtmove', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    vel = Twist()
    ang_vel = paramet_angl(ang_vel)

    while not rospy.is_shutdown():
        pub.publish(speed_paramet(vel, linvel = line_vel))
        rate.sleep()
        pub.publish(speed_paramet(vel, angvel = ang_vel))
        rate.sleep()


if __name__ == '__main__':
    move_tertle(2,90)

