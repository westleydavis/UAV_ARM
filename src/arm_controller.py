#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from keyboard.msg import Key
from uav_arm.msg import jointAngles

mymsg = jointAngles()
# from keyboard import Key.msg

mode = 0
# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim


# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

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
