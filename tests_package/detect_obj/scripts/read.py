#!/usr/bin/env python

import rospy
import os
import os.path
import cv2
from std_msgs.msg import String

def callback(data):
    
    file_name = "show.jpg"
            
    current_file = os.path.realpath(__file__)
    current_file = os.path.dirname(current_file)

    data_folder = "./Images"
    data_folder = os.path.join(current_file, data_folder) 
            
    img_path = os.path.join(data_folder, file_name) 
    
    if os.path.isfile(img_path):
        img = cv2.imread(img_path)
        cv2.imshow("Object",img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        
        os.remove(img_path)
        
        
    
def listener():
    rospy.init_node('listener')
    rospy.Subscriber("show_img", String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()