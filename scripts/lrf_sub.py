#!/usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan

def scanCallback(message):
    dist_data=list(message.ranges)
    minimum=min(dist_data)
    min_idx=dist_data.index(minimum)
    print(f"最短距離はインデックスNo.{min_idx}の{minimum}です。")


rospy.init_node("listner_scan")
sub=rospy.Subscriber("scan",LaserScan,scanCallback)

rospy.spin()