#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from keyboard.msg import Key
from uav_arm.msg import jointAngles
from std_msgs.msg import string

mymsg = jointAngles()


mode = 0


class Servo:

    def __init__(self, name):
        self.name = name
        pub = rospy.Publisher('turtle1/cmd_vel', Twist)

    def move(self, position):
        self.position = position


servo1 = Servo()
Servo servo2
Servo servo3
Servo servo4
Servo servo5


def callback(data):
    twist = Twist()
    if mode == 0:
        modeinv = 1
    else:
        modeinv = 0
    # vertical left stick axis = linear rate
    twist.linear.x = 4*data.axes[mode]
    # horizontal left stick axis = turn rate
    twist.angular.z = 4*data.axes[modeinv]
    pub.publish(twist)


def callback2(data):
    # key = Key()
    global mode

    myinput = data.code
    if myinput == Key.KEY_F1:
        mode = 1
    elif myinput == Key.KEY_F2:
        mode = 0


# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('turtle1/cmd_vel', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # subscribed to keyboard inputs on the topic "keyboard"
    rospy.Subscriber("keyboard/keydown", Key, callback2)
    # starts the node
    rospy.init_node('Joy2Turtle')
    rospy.spin()


if __name__ == '__main__':
    start()
