#! /usr/bin/env python3
from logging import shutdown
import rospy 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

def position(begg):
    global initialx, initialy, initialtheta
    initialx = begg.x
    initialy = begg.y
    initialtheta = begg.theta

def linear(go2x,go2y):
    variacao_x = go2x - initialx
    variacao_y = go2y - initialy
    distance = sqrt(variacao_x **2 + variacao_y**2)
    return distance

def angular(go2x, go2y):
    variacao_x = go2x - initialx
    variacao_y = go2y - initialy
    theta = atan2(variacao_y,variacao_x)
    angular_distance = theta - initialtheta
    return angular_distance

if __name__=="__main__":
    rospy.init_node("turtlecode")
    pub =  rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    sub =  rospy.Subscriber('turtle1/pose', Pose, position)

    msg = Twist()
    local = Pose()

    x_init = float(input("Escreva o destino X:\n"))
    y_init = float(input("Escreva o destino Y:\n"))

    loopfreq = rospy.Rate(10)

    
    while not rospy.is_shutdown():
        msg.linear.x = linear(x_init, y_init) * 1.5
        msg.angular.z  = angular(x_init, y_init) * 6
        pub.publish(msg)

        loopfreq.sleep()

        if msg.linear.x <= 0.1:
            break




    

    




