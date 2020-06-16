#!/usr/bin/env python

import math
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from SM_movement import SM_movement
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time

fig=True
r_st=""
go=0

class movement_node:

    def __init__(self, pub, estaciones, pub_done):
        self._pub=pub
        self._estaciones=estaciones
        self._pub_done=pub_done
        self.angle_target=0
        self.dist_target=0

    def position_notify(self,msg):

        global go
        global fig
        global r_st

        mv_control=SM_movement(self._pub)
        x=msg.pose.pose.position.x
        y=msg.pose.pose.position.y
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list)

        dist_actual=math.sqrt(x*x+y*y)

        if (yaw<0):
            yaw=(2*math.pi)+yaw

        angle_origin=math.pi+self.angle_target
        dist_origin=0

        if (self.angle_target>2*math.pi):
            self.angle_target-=(2*math.pi)

        if (angle_origin>2*math.pi):
            angle_origin-=(2*math.pi)

        if (self.angle_target==0 and yaw>=math.pi):
            self.angle_target=2*math.pi
        else:
            angle_target=0

        if (go==1):
            r_st,delay=mv_control.SM_states(self._pub,True,yaw,self.angle_target,angle_origin,self.dist_target,dist_origin,dist_actual)
            rospy.loginfo('State: {}'.format(r_st))
            time.sleep(delay)

        if (r_st=="Ready" and (go==1)):
            go=0
            if fig==True:
                self._pub_done.publish("Ready")
                fig=False
            rospy.loginfo('Wating for a new piece')
                
        elif (r_st!="Ready" and go==0):
            self._pub_done.publish("Ready")
            rospy.loginfo('Wating first piece')

    def element_selection(self,msg):
        global fig
        global go

        msg=msg.data

        if (msg!="Done"):

            if(msg!="unidentified"):

                for e_name, e_x, e_y in self._estaciones:
                    print("Mensaje: ", msg)
                    print("e_name: ",msg)

                    if (e_name==msg):

                        self.dist_target=math.sqrt(e_x*e_x+e_y*e_y)
                        self.angle_target=math.atan(e_y/(e_x+0.0000001))

                        if (self.angle_target<0):
                            self.angle_target+=(2*math.pi)
                        go=1
                        fig=True
            else:
                rospy.loginfo(' Unidentified element')
                go=0
                fig=True

        else:
            rospy.loginfo('Finish')
            go=0
            fig=False

def main():

    estaciones=[]
    estaciones.append(("wood_rectangle", 2, 2))
    estaciones.append(("red_rectangle", 2, 0))
    estaciones.append(("triangle", -2, 2))
    estaciones.append(("square", 0, -2))
    estaciones.append(("bridge", 0, 2))

    rospy.init_node('robot_move')
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    pub_done = rospy.Publisher('/robot_status',String, queue_size=10)
    rate=rospy.Rate(1)

    monitor=movement_node(pub, estaciones, pub_done)

    rospy.Subscriber("/odom", Odometry, monitor.position_notify)
    rospy.Subscriber("obj_detector", String, monitor.element_selection)

    while not rospy.is_shutdown():

        rate.sleep()

if __name__ == '__main__':

    main()
