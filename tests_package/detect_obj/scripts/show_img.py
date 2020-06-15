#!/usr/bin/env python

import rospy
import os
import os.path
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

class ShowImg(object):
    def __init__(self,pub):
        self._pub=pub

    def callback(self,data):

        img_path = data.data

        if os.path.isfile(img_path):
            img = cv2.imread(img_path)
            bridge = CvBridge()
            img_msg = bridge.cv2_to_imgmsg(img, encoding="passthrough")
            self._pub.publish(img_msg)

            os.remove(img_path)


def listener():
    rospy.init_node('show_img')

    pub = rospy.Publisher('img_rviz', Image, queue_size=10)
    imgObj = ShowImg(pub)
    rospy.Subscriber("ready_img", String, imgObj.callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
