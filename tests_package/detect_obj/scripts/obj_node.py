#!/usr/bin/env python
  
import rospy
import os.path
import cv2
import sys
import random
import numpy as np
from std_msgs.msg import String
   
def identifier(i):
    
    file_name = str(i) + ".jpg"
    data_folder = "/home/tini/Documents/Imagenes/"
    img_path = os.path.join(data_folder, file_name) 
    
    if os.path.isfile(img_path):
        
        img = cv2.imread(img_path)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret,imgBin = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY)
        im2,contours,hierarchy = cv2.findContours(imgBin, 1, 2)
    
        areasVal = []
        shape = ""
	
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])  
            areasVal.append(area)
    
        objIndex = areasVal.index(max(areasVal))
        obj = contours[objIndex]
   
        M = cv2.moments(obj)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.drawContours(img, contours, objIndex, (0, 255, 0), 2)
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    
        peri = cv2.arcLength(obj, True)
        approx = cv2.approxPolyDP(obj, 0.04 * peri, True)
    
        if len(approx) == 3:
            shape = "triangle"

        elif len(approx) == 5:
            shape = "bridge"
        
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.95 and ar <= 1.05:
                shape = "square"
            
            else: 
                mask = np.zeros(imgGray.shape, np.uint8)
                cv2.drawContours(mask, obj, -1, (255), 1)
                mean = cv2.mean(imgGray, mask=mask)
            
                if mean[0] > 59:
                    shape = "wood_rectangle"
                elif mean[0] > 56 and mean[0] < 59:
                    shape = "red_rectangle"
                else:
                    shape = "white_rectangle"
                
        else:
            shape = "unidentified"
    
    else:
        shape = "unidentified"
    
    return shape
    
def main():    
    pub = rospy.Publisher('obj_detector', String, queue_size=10)
    rospy.init_node('obj_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    img_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    random.shuffle(img_list)
    
    while not rospy.is_shutdown():
         obj_detected = identifier(17)
         rospy.loginfo(obj_detected)
         pub.publish(obj_detected)
         rate.sleep()
 


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass