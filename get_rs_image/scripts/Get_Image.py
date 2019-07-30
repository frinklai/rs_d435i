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
            rospy.init_node('get_image_from_rs_d435i', anonymous=True)
            self.bridge = CvBridge()
            self.image = np.zeros((0,0,3), np.uint8)
            self.take_picture_counter = 0
            # self.mtx = np.load('/home/iclab-arm/AI_Bot_ws/src/AI_Bot/vision/get_image/scripts/'+'camera_calibration_mtx.npy')
            # self.dist = np.load('/home/iclab-arm/AI_Bot_ws/src/AI_Bot/vision/get_image/scripts/'+'camera_calibration_dist.npy')
            # self.newcameramtx = np.load('/home/iclab-arm/AI_Bot_ws/src/AI_Bot/vision/get_image/scripts/'+'camera_calibration_newcameramtx.npy')
            # self.dst_roi_x, self.dst_roi_y, self.dst_roi_w, self.dst_roi_h  = np.load('/home/iclab-arm/AI_Bot_ws/src/AI_Bot/vision/get_image/scripts/'+'camera_calibration_roi.npy')

            #s = rospy.Service("request FLIR", FLIR_image, self.service_callback)
            
            
            # rospy.Subscriber("/camera/image_color", Image, self.callback)
            rospy.Subscriber("/camera/color/image_raw", Image, self.callback)
            self.cv_image = None

            rospy.spin()

    def callback(self, data):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            # self.cv_image = image
            # self.un_dst_img = cv2.undistort(self.cv_image, self.mtx, self.dist, None, self.newcameramtx)
            # self.un_dst_img = self.un_dst_img[self.dst_roi_y:self.dst_roi_y+self.dst_roi_h, \
            #         self.dst_roi_x:self.dst_roi_x+self.dst_roi_w]
        except CvBridgeError as e:
            print(e)
        # print('show img')
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", self.cv_image)
        self.get_image(self.cv_image)
        cv2.waitKey(1)
    
    def get_image(self, crop_image):
        if cv2.waitKey(33) & 0xFF == ord('s'):
            #name = str(Train_Data_Dir + str(datetime.datetime.now()) + '_' + Object_Name + '_' + str(self.take_picture_counter+1) + ".jpg")
            name = str(Train_Data_Dir + str(Object_Name + '_' + str(self.take_picture_counter+1) + ".jpg"))
            cv2.imwrite(name,crop_image)
            print("[Save] ", name)
            self.take_picture_counter += 1
        else:
            pass

if __name__ == '__main__':

    print('python version is: ', sys.version)
    listener = Get_image()
    cv2.destroyAllWindows()
