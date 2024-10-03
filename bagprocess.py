import rosbag
import os
import argparse
import yaml
import numpy as np
import torch
from tf import TransformListener
from std_msgs.msg import Int32, String
import rospy
from typing import List
from tf.transformations import euler_from_quaternion
from pathlib import Path
import subprocess
from math import radians, sin, cos, sqrt, atan2
import ipdb 
import csv

folder_Path =  os.getcwd()

data_path = folder_Path + "/datasets/cse571_project/fresh_data/odometry_data.csv"
data_path2 = folder_Path + "/datasets/cse571_project/fresh_data/imu_data.csv"
output_path =  folder_Path + "/datasets/cse571_project/fresh_data/groundtruth.txt"
output_path2 = folder_Path + "/datasets/cse571_project/fresh_data/accelerometer.txt"
# ipdb.set_trace()

# files = os.listdir(data_path)

# png_files = [file for file in files if file.endswith('.png')]
# png_files.sort()

# def conv_filename(filename):
#     base_name  = filename[:-4]
#     new_name = f"{base_name[6:16]}.{base_name[16:]}"
#     return new_name

# with open(output_path, 'w') as f:
#     for png_file in png_files:
#         conv = conv_filename(png_file)
#         f.write(f"{conv} depth/{png_file[:-4]}.png\n")

selected_columns = [0,1,2,3]
selected_columns2 = [1,2,3,4]
selected_columns3 = [0,8,9,10]
# column_widths =    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
with open(data_path2, mode='r', newline='') as csv_file:
    # with open(data_path2, mode='r', newline='') as csv_file2:
    csv_reader = csv.reader(csv_file)
        # csv_reader2 = csv.reader(csv_file2)
    header = next(csv_reader)
        # header2 = next(csv_reader2)

    selected_header = [header[i] for i in selected_columns3]
        # selected_header2 = [header2[i] for i in selected_columns2]
            
    with open(output_path2, mode='w') as text_file:
        header_line = ' '.join(f"{selected_header[i]:}" for i in range(len(selected_columns3)))
        # header_line2 = ' '.join(f"{selected_header2[i]:}" for i in range(len(selected_columns2)))
        text_file.write(header_line + '\n')
        for row in csv_reader:
            selected_row = [row[i] for i in selected_columns3]
            # selected_row2 = [row2[i] for i in selected_columns2]
            row_line = ' '.join(f"{selected_row[i]:}" for i in range(len(selected_columns3)))
            # row_line2 = ' '.join(f"{selected_row2[i]:}" for i in range(len(selected_columns2)))
            text_file.write(row_line + '\n')

