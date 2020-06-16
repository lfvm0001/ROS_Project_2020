#!/usr/bin/env python

import roslib; roslib.load_manifest('visualization_marker_tutorials')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math

topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray,queue_size=10)

rospy.init_node('register')

markerArray = MarkerArray()
put=0

while not rospy.is_shutdown():

   marker_wood_rectangle = Marker()
   marker_wood_rectangle.header.frame_id = "/odom"
   marker_wood_rectangle.type = marker_wood_rectangle.CUBE
   marker_wood_rectangle.action = marker_wood_rectangle.ADD
   marker_wood_rectangle.scale.x = 0.5
   marker_wood_rectangle.scale.y = 0.5
   marker_wood_rectangle.scale.z = 0.2
   marker_wood_rectangle.color.a = 1.0
   marker_wood_rectangle.color.r = 255.0
   marker_wood_rectangle.color.g = 255.0
   marker_wood_rectangle.color.b = 0.0
   marker_wood_rectangle.pose.orientation.w = 0.923879
   marker_wood_rectangle.pose.orientation.z = 0.382683
   marker_wood_rectangle.pose.orientation.y=0.0
   marker_wood_rectangle.pose.orientation.x=0.0
   marker_wood_rectangle.pose.position.x = 2.25
   marker_wood_rectangle.pose.position.y = 2.25
   marker_wood_rectangle.pose.position.z = 0.1

   marker_red_rectangle = Marker()
   marker_red_rectangle.header.frame_id = "/odom"
   marker_red_rectangle.type = marker_red_rectangle.CUBE
   marker_red_rectangle.action = marker_red_rectangle.ADD
   marker_red_rectangle.scale.x = 0.5
   marker_red_rectangle.scale.y = 0.5
   marker_red_rectangle.scale.z = 0.2
   marker_red_rectangle.color.a = 1.0
   marker_red_rectangle.color.r = 255.0
   marker_red_rectangle.color.g = 0.0
   marker_red_rectangle.color.b = 0.0
   marker_red_rectangle.pose.orientation.w = 1.0
   marker_red_rectangle.pose.orientation.z = 0.0
   marker_red_rectangle.pose.orientation.y=0.0
   marker_red_rectangle.pose.orientation.x=0.0
   marker_red_rectangle.pose.position.x = 2.3
   marker_red_rectangle.pose.position.y = 0
   marker_red_rectangle.pose.position.z = 0.1

   marker_square = Marker()
   marker_square.header.frame_id = "/odom"
   marker_square.type = marker_wood_rectangle.CUBE
   marker_square.action = marker_wood_rectangle.ADD
   marker_square.scale.x = 0.5
   marker_square.scale.y = 0.5
   marker_square.scale.z = 0.2
   marker_square.color.a = 1.0
   marker_square.color.r = 0.0
   marker_square.color.g = 255.0
   marker_square.color.b = 0.0
   marker_square.pose.orientation.w = 1.0
   marker_square.pose.orientation.z=0.0
   marker_square.pose.orientation.y=0.0
   marker_square.pose.orientation.x=0.0
   marker_square.pose.position.x = 0
   marker_square.pose.position.y = -2.3
   marker_square.pose.position.z = 0.1

   marker_bridge = Marker()
   marker_bridge.header.frame_id = "/odom"
   marker_bridge.type = marker_wood_rectangle.CUBE
   marker_bridge.action = marker_wood_rectangle.ADD
   marker_bridge.scale.x = 0.5
   marker_bridge.scale.y = 0.5
   marker_bridge.scale.z = 0.2
   marker_bridge.color.a = 1.0
   marker_bridge.color.r = 150
   marker_bridge.color.g = 0.0
   marker_bridge.color.b = 0.0
   marker_bridge.pose.orientation.w = 1.0
   marker_bridge.pose.orientation.z=0.0
   marker_bridge.pose.orientation.y=0.0
   marker_bridge.pose.orientation.x=0.0
   marker_bridge.pose.position.x = 0
   marker_bridge.pose.position.y = 2.3
   marker_bridge.pose.position.z = 0.1

   marker_triangle = Marker()
   marker_triangle.header.frame_id = "/odom"
   marker_triangle.type = marker_wood_rectangle.CUBE
   marker_triangle.action = marker_wood_rectangle.ADD
   marker_triangle.scale.x = 0.5
   marker_triangle.scale.y = 0.5
   marker_triangle.scale.z = 0.2
   marker_triangle.color.a = 1.0
   marker_triangle.color.r = 0.0
   marker_triangle.color.g = 0.0
   marker_triangle.color.b = 255
   marker_triangle.pose.orientation.w = 0.923879
   marker_triangle.pose.orientation.z = -0.382683
   marker_triangle.pose.orientation.y=0.0
   marker_triangle.pose.orientation.x=0.0
   marker_triangle.pose.position.x = 2.25
   marker_triangle.pose.position.y = -2.25
   marker_triangle.pose.position.z = 0.1

   marker_storage = Marker()
   marker_storage.header.frame_id = "/odom"
   marker_storage.type = marker_wood_rectangle.CUBE
   marker_storage.action = marker_wood_rectangle.ADD
   marker_storage.scale.x = 0.2
   marker_storage.scale.y = 1.5
   marker_storage.scale.z = 0.1
   marker_storage.color.a = 1.0
   marker_storage.color.r = 0
   marker_storage.color.g = 0
   marker_storage.color.b = 0
   marker_storage.pose.orientation.w = 1
   marker_storage.pose.orientation.z = 0.0
   marker_storage.pose.orientation.y=0.0
   marker_storage.pose.orientation.x=0.0
   marker_storage.pose.position.x = -0.25
   marker_storage.pose.position.y = 0
   marker_storage.pose.position.z = 0.05

   # We add the new marker to the MarkerArray, removing the oldest
   # marker from it when necessary

   markerArray.markers.append(marker_wood_rectangle)
   markerArray.markers.append(marker_red_rectangle)
   markerArray.markers.append(marker_square)
   markerArray.markers.append(marker_triangle)
   markerArray.markers.append(marker_bridge)
   markerArray.markers.append(marker_storage)

   # Renumber the marker IDs
   id = 0
   for m in markerArray.markers:
       m.id = id
       id += 1

   # Publish the MarkerArray
   if put<5:
       publisher.publish(markerArray)
       put+=1
   else:
       put=put


   rospy.sleep(1)
