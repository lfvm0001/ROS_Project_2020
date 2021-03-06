#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist

current_state=0
going=True
dir=""

class SM_movement:

    def __init__(self,pub):
        self._pub=pub

    def get_dir(self,angle_goal,angle_robot):

        if (angle_goal>=angle_robot):
            comp_target=2*math.pi-angle_goal
            sub_arc=abs(angle_robot-angle_goal)
            sum_arc=comp_target+angle_robot
        else:
            comp_target=2*math.pi-angle_robot
            sub_arc=abs(angle_robot-angle_goal)
            sum_arc=comp_target+angle_goal

        if (angle_goal>=angle_robot):
            if (sub_arc<sum_arc):
                dir="pos"
            else:
                dir="neg"

        else:
            if (sub_arc<sum_arc):
                dir="neg"
            else:
                dir="pos"

        return dir

    def movement_cmd(self, rot_trans, dir, speed):

        vel=Twist()

        vel.linear.x=0.0
        vel.linear.y=0.0
        vel.linear.z=0.0

        vel.angular.x=0.0
        vel.angular.y=0.0
        vel.angular.z=0.0

        if (rot_trans==False and dir=="pos"):
            vel.angular.z=speed

        elif (rot_trans==False and dir=="neg"):
            vel.angular.z=-speed

        elif (rot_trans==True):
            vel.linear.x=speed

        elif (dir=="stop"):
            print("Positioning piece")

        self._pub.publish(vel)

    def SM_states(self,pub,start,yaw,angle_target,angle_origin,dist_target,dist_origin,dist_actual):

        global current_state
        global going
        global dir

        delay=0

        ###################Logica de los estados#########################
        if (current_state==0):
            going=True
            if start==True:
                next_state=1
            else:
                next_state=0
            state_output=0

        elif(current_state==1):
            if (going==True):
                dir=self.get_dir(angle_target,yaw)
            else:
                dir=self.get_dir(angle_origin,yaw)
            next_state=2
            state_output=1

        elif(current_state==2):
            if (going==True):
                if(abs(angle_target-yaw)>0.1):
                    next_state=2
                else:
                    next_state=3
            state_output=2

        elif(current_state==3):
            if (going==True):
                if(abs(angle_target-yaw)>0.005):
                    next_state=3
                else:
                    next_state=4
            state_output=3

        elif(current_state==4):
            if ((going==True) and (abs(dist_target-dist_actual)>0.025)):
                next_state=4
            elif ((going==False) and (abs(dist_origin-dist_actual)>0.025)):
                next_state=4
            else:
                next_state=5
            state_output=4

        elif(current_state==5):
            if (going==False):
                next_state=6
            else:
                delay=5
                going=False
                next_state=4
            state_output=5

        elif(current_state==6):
            going==True
            next_state=0
            state_output=6

        else:
            next_state=0

        ######################## Salidas ##################################

        if (state_output==0):

            output="Waiting request"

        elif (state_output==1):

            output='Getting path'
            delay=5

        elif (state_output==2):

            output='Rotating'
            speed=0.5
            self.movement_cmd(False,dir,speed)

        elif (state_output==3):

            output='Fine rotating'
            speed=0.05
            self.movement_cmd(False,dir,speed)

        elif (state_output==4):

            output='Moving'
            speed=0.3
            if (going==False):
                self.movement_cmd(True,dir,-speed)
            else:
                self.movement_cmd(True,dir,speed)

        elif (state_output==5):

            output='Leaving piece'
            self.movement_cmd(True,"stop",0)

        elif (state_output==6):

            output='Ready'
            self.movement_cmd(True,"stop",0)

        current_state=next_state
        return output, delay
