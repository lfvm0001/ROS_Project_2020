#!/usr/bin/env python
  
import rospy
from std_msgs.msg import String



def main():    
    rospy.init_node('writter', anonymous=True)
    pub = rospy.Publisher('ready_flag', String, queue_size=10)
    
    r = rospy.Rate(0.1) 
    i=1
    
    while i<20:
        pub.publish("Ready")
        rospy.loginfo("Ready")
        i += 1
        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass