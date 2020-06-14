#!/usr/bin/env python

import rospy
import os
import os.path
import cv2
from std_msgs.msg import String

def callback(data):
    
    img_path = data.data
    
    if os.path.isfile(img_path):
        img = cv2.imread(img_path)
        cv2.imshow("Object",img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        
        os.remove(img_path)
   

def listener():
    rospy.init_node('listener_node')
    rospy.Subscriber("show_img", String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()