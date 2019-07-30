#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# sys.path.insert(1, "/usr/local/lib/python3.5/dist-packages/")

sys.path.insert(1, "/home/iarc/.local/lib/python3.5/site-packages/")
# sys.path.insert(0, '/opt/installer/open_cv/cv_bridge/lib/python3/dist-packages/')
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from get_rs_image.srv import *
import datetime 
#sys.path.insert(1, "/home/iclab-arm/.local/lib/python3.5/site-packages/") 
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import time 
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--Object_Name', type=str, default='.', help='Class name of training object.')
FLAGS = parser.parse_args()

Object_Name = FLAGS.Object_Name
Train_Data_Dir = os.path.dirname(os.path.realpath(__file__)) + '/Training_Data/' + \
    str(datetime.datetime.now()) + '_' + Object_Name + '/'


class Get_image():
    def __init__(self):
            
        self.bridge = CvBridge()
        self.image = np.zeros((0,0,3), np.uint8)
        self.depth = np.zeros((0,0,3), np.uint8)
        self.take_picture_counter = 0

        rospy.Subscriber("/camera/color/image_raw", Image, self.rgb_callback)
        # rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.depth_callback)
        # rospy.Subscriber("/camera/aligned_depth_to_infra1/image_raw", Image, self.depth_callback)
        # rospy.Subscriber("/camera/infra1/image_rect_raw", Image, self.depth_callback) 

        rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, self.depth_callback)

        self.cv_image = None
        self.cv_depth = None
        self.display_mode = 'rgbd'

            

    def show_image(self):
        image_dim = np.asarray(self.cv_image).shape
        depth_dim = np.asarray(self.cv_depth).shape
        # print(type(self.cv_depth))
        
        if(self.display_mode=='rgb'):
            cv2.imshow("rgb result", self.cv_image)

        elif(self.display_mode=='depth'):
            cv2.imshow("depth result", self.cv_depth)

        elif(self.display_mode=='rgbd'):
            if(image_dim == depth_dim):
                rgbd_images = np.hstack((self.cv_image, self.cv_depth))
                cv2.imshow("rgbd result", rgbd_images)
            # else:
            #     print('dim error')
        else:
            print('unknow mode')
            pass
        

        cv2.waitKey(1)

    def rgb_callback(self, data):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")    # for rgb image

        except CvBridgeError as e:
            print(e)

        if(self.display_mode=='rgb')or(self.display_mode=='rgbd'):
            self.show_image()   
        # cv2.imshow("rgb result", self.cv_image)
        # cv2.waitKey(1)

    def depth_callback(self, data):
        try:
            self.cv_depth = self.bridge.imgmsg_to_cv2(data, "16UC1")    # for depth image 16UC1
            self.cv_depth = cv2.applyColorMap(cv2.convertScaleAbs(self.cv_depth, alpha=0.03), cv2.COLORMAP_JET)

        except CvBridgeError as e:
            print(e)
        if(self.display_mode=='depth'):
            self.show_image()
        # cv2.imshow("depth result", self.cv_depth)
        # cv2.waitKey(1)


    

if __name__ == '__main__':

    print('python version is: ', sys.version)
    rospy.init_node('get_image_from_rs_d435i', anonymous=True)
    listener = Get_image()
    rospy.spin()
    cv2.destroyAllWindows()
    
