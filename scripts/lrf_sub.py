#!/usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

def idx_to_deg(idx,message):
    deg=message.angle_increment*idx*180/np.pi-135
    return int(deg) #分解能が0.22度なので、とりま整数

def scanCallback(message):
    dist_data=list(message.ranges)
    angle_min_data=message.angle_min
    angle_max_data=message.angle_max
    minimum=min(dist_data)
    min_idx=dist_data.index(minimum)
    print(f"最短距離:{idx_to_deg(min_idx,message)}度 最短距離:{round(minimum,5)}m")
    #print(angle_min_data,angle_max_data)
    header_data=message.header
    #print(type(header_data))
    angle_increment_data=message.angle_increment
    #print(angle_increment_data)
    time_increment_data=message.time_increment
    #print(time_increment_data)
    scan_time_data=message.scan_time
    #print(scan_time_data)
    range_min_data=message.range_min
    range_max_data=message.range_max
    #print(range_min_data,range_max_data)
    intensities_data=list(message.intensities)
    #print(max(intensities_data))


rospy.init_node("listner_scan")
sub=rospy.Subscriber("scan",LaserScan,scanCallback)

rospy.spin()

#Windowsから編集してみた
#Ubuntuでも上記編集を確認できました