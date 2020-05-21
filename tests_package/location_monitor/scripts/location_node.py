#!/usr/bin/env python

import rospy 
import math
from nav_msgs.msg import Odometry
from location_monitor.msg import LandmarkDistance

def distance (x1,y1,x2,y2):
    xd= x1-x2
    yd= y1-y2
    return math.sqrt(xd*xd+yd*yd)

class LandmarkMonitor(object):
    def __init__(self, pub, landmarks):
        self._landmarks=landmarks
        self._pub=pub

    def callback (self, msg):
        x=msg.pose.pose.position.x
        y=msg.pose.pose.position.y
        closest_name= None
        closest_distance= None
        for l_name, l_x, l_y in self._landmarks:
            dist=distance(x,y,l_x,l_y)
            if closest_distance is None or dist<closest_distance:
                closest_name=l_name
                closest_distance=dist
        ld=LandmarkDistance()
        ld.name=closest_name
        ld.distance=closest_distance
        self._pub.publish(ld)
        rospy.loginfo('Closest: {}'.format(closest_name))
    

def main():
    rospy.init_node('location_monitor')
    
    landmarks=[]
    landmarks.append(("bookshelf", -1.36, 3.43))
    landmarks.append(("dumpster", -5.71, 0.53))
    landmarks.append(("cinder_block", 2.76, -0.20))
    landmarks.append(("cabinet", -0.20, -3.11))
    
    pub=rospy.Publisher('Closest_landmark', LandmarkDistance, queue_size=10)
    monitor=LandmarkMonitor(pub,landmarks)
    
    rospy.Subscriber("/odom", Odometry, monitor.callback)
    rospy.spin()


if __name__ == '__main__':
    
    main()
