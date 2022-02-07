#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float64
import math,time

class serialize_bit:
    def __init__(self,codeset):
        self.codeset = codeset


    def serialize(self,data):
        rezult_serialize = data.encode(self.codeset)
        return rezult_serialize


    def de_serialize(self,data):
        rezult_deserialize = data.decode(self.codeset)
        return rezult_deserialize

class teleop_serial():
    def __init__(self):
        rospy.init_node("my_subscriber_node", anonymous = True)
        my_subscriber = rospy.Subscriber("/turtle1/cmd_vel", Twist, self.callback)
        self.put_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        self.command = Twist()
        self.serialize_bit = serialize_bit('utf-8')
        self.rate = rospy.Rate(10)
        rospy.spin()


    def callback(self,data):
        self.Linear_x = str(data.linear.x)
        self.Angular_z = str(data.angular.z)
        self.String_value = (self.Linear_x + ":" + self.Angular_z)
        self.Bit_string_value = self.serialize_bit.serialize(self.String_value)
        self.After_de_serial = self.serialize_bit.de_serialize(self.Bit_string_value)

        self.Linear_deser_x = self.After_de_serial.split(':')[0]
        self.Angular_deser_z = self.After_de_serial.split(':')[1]
        self.command.linear.x = float(self.Linear_deser_x)
        self.command.angular.z = float(self.Angular_deser_z)

        self.put_publisher.publish(self.command)
        #self.command.linear.x = 0
        #self.command.angular.z = 0
        #self.put_publisher.publish(self.command)

        print("------------")
        print(data.linear.x)
        print(data.angular.z)
        print("------------")
        print(self.Bit_string_value)
        print("------------")
        print(self.After_de_serial)
        print("Delenie stroc")
        print(self.Linear_deser_x)
        print(self.Angular_deser_z)

if __name__=="__main__":
    try:
        x = teleop_serial()
        x.callback()
    except rospy.ROSInterruptException:
        pass