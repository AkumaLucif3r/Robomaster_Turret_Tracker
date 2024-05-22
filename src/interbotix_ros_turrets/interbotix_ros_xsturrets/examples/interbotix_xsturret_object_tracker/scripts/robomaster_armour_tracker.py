#!/usr/bin/env python

import argparse
import math
import cv2
import rospy
import csv
from ultralytics import YOLO
import numpy as np

from sensor_msgs.msg import Image, JointState
from geometry_msgs.msg import Pose, PoseArray, Vector3
from interbotix_xs_msgs.msg import JointGroupCommand
from interbotix_xs_msgs.srv import RobotInfo
from cv_bridge import CvBridge, CvBridgeError

print("Loading model...", end='')
model = YOLO("/home/ben/interbotix_ws/src/interbotix_ros_turrets/interbotix_ros_xsturrets/examples/interbotix_xsturret_object_tracker/scripts/best_1.pt")
print("Done!")

class ColorTracker(object):
    def __init__(self):
                                                                                                                                                                    
                 
        self.center_x = 320/2.0                                                                                         
        self.center_y = 240/2.0                                                                                         
        self.cv_image = None                                                                                            
        self.joint_states = None                                                                                        
        self.bridge = CvBridge()                                                                                        
        rospy.wait_for_service("get_robot_info")                                                                        
        self.srv_robot_info = rospy.ServiceProxy("get_robot_info", RobotInfo)                                           
        self.pub_cmds = rospy.Publisher("commands/joint_group", JointGroupCommand, queue_size=1)                        
        self.publish_contour_detections_image = rospy.get_param('~publish_contour_detections_image')                    
        if (self.publish_contour_detections_image):
            self.pub_images = rospy.Publisher("contour_detections", Image, queue_size=5)                                
        self.sub_joint_states = rospy.Subscriber("joint_states", JointState, self.joint_state_cb)                       
        while (self.joint_states is None): pass                                                                         
        self.joint_commands = JointGroupCommand("turret", list(self.joint_states.position))                             
        self.robot_info = self.srv_robot_info("group", "turret")                                                        
        self.sub_img = rospy.Subscriber("lifecam/image_raw", Image, self.image_cb)                                      

    ### @brief ROS Subscriber callback function to get updated joint states
    ### @param msg - updated JointState message
    def joint_state_cb(self, msg):
        self.joint_states = msg

    ### @brief ROS Subscriber callback function to get the latest images from the 'usb_cam' node
    ### @param msg - updated Image message
    def image_cb(self, msg):
        try:
          cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
          print(e)

        
        results = model(cv_image, stream=True, verbose=False)

    	poses = PoseArray()
    	height, width, _ = cv_image.shape

    	clx, cly = -3000000, -3000000
    	distance = math.sqrt(clx ** 2 + cly ** 2)

   	 # for box in results[0].boxes:
    	for x in results:
        	for box in x.boxes:
        	    if box.conf[0] < min_conf:
                	continue

            	x1, y1, x2, y2 = box.xyxy[0]
            	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            	cx = math.floor((x2 - x1) / 2 + x1)
            	cy = math.floor((y2 - y1) / 2 + y1)

            	dcx = abs(cx - width)
            	dcy = abs(cy - height)
            	d = math.sqrt(dcx ** 2 + dcy ** 2)
            	if d < distance:
               	clx, cly = cx, cy
                	distance = d

            	cv2.draw_box(cv_image, x1, y1, x2, y2)
            	cv2.draw_circle(cv_image, cx, cy, 4)
            	cv2.draw_line(cv_image, cx, cy, math.floor(width / 2), math.floor(height / 2))
		
        	if not (clx < 0 or cly < 0):
            		draw_line(cv_image, clx, cly, math.floor(width / 2), math.floor(height / 2), (0, 0, 255))
            	

            # Publish JointCommands so that the center pixel in the image overlaps the red circle mentioned above
            if ((self.center_x - cx) > 10):
                self.joint_commands.cmd[0] += 0.02
                if (self.joint_commands.cmd[0] > self.robot_info.joint_upper_limits[0]):
                    self.joint_commands.cmd[0] = self.robot_info.joint_upper_limits[0]
            elif ((self.center_x - cx) < -10):
                self.joint_commands.cmd[0] -= 0.02
                if (self.joint_commands.cmd[0] < self.robot_info.joint_lower_limits[0]):
                    self.joint_commands.cmd[0] = self.robot_info.joint_lower_limits[0]
            if ((self.center_y - cy) > 10):
                self.joint_commands.cmd[1] -= 0.02
                if (self.joint_commands.cmd[1] < self.robot_info.joint_lower_limits[1]):
                    self.joint_commands.cmd[1] = self.robot_info.joint_lower_limits[1]
            elif ((self.center_y - cy) < -10):
                self.joint_commands.cmd[1] += 0.02
                if (self.joint_commands.cmd[1] > self.robot_info.joint_upper_limits[1]):
                    self.joint_commands.cmd[1] = self.robot_info.joint_upper_limits[1]
            self.pub_cmds.publish(self.joint_commands)

        # if the overlay image should be published...
        if (self.publish_contour_detections_image):
            cv_overlay = cv_image
            try:
                self.pub_images.publish(self.bridge.cv2_to_imgmsg(cv_overlay, "bgr8"))
            except CvBridgeError as e:
                print(e)

if __name__ == '__main__':
    rospy.init_node('xsturret_color_tracker')
    color_tracker = ColorTracker()
    rospy.spin()
