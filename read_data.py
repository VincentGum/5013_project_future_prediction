# -*- coding: utf-8 -*-

import pandas as pd
import h5py
import os
import numpy as np
import matplotlib.pyplot as plt


def data():
    data_path = '/Users/ganweisen/PycharmProjects/MSBD 5013/python platform/Data/'

    # info_name = "information.csv"
    # info_path = data_path + info_name
    # info = pd.read_csv(info_path, encoding='utf-8')

    data_name_1_1 = "data_format1_20170717_20170915.h5"
    data_name_2_1 = "data_format2_20170918_20170922.h5"
    data_name_1_2 = "data_format1_20170925_20170929.h5"
    data_name_2_2 = "data_format2_20170717_20170915.h5"
    data_name_1_3 = "data_format1_20170918_20170922.h5"
    data_name_2_3 = "data_format2_20170925_20170929.h5"

    data_path_1_1 = data_path + data_name_1_1
    data_path_2_1 = data_path + data_name_2_1
    data_path_1_2 = data_path + data_name_1_2
    data_path_2_2 = data_path + data_name_2_2
    data_path_1_3 = data_path + data_name_1_3
    data_path_2_3 = data_path + data_name_2_3

    btData_1_1 = h5py.File(data_path_1_1, mode='r')
    btData_2_1 = h5py.File(data_path_2_1, mode='r')
    btData_1_2 = h5py.File(data_path_1_2, mode='r')
    btData_2_2 = h5py.File(data_path_2_2, mode='r')
    btData_1_3 = h5py.File(data_path_1_3, mode='r')
    btData_2_3 = h5py.File(data_path_2_3, mode='r')

    keys_1_1 = list(btData_1_1.keys())
    # keys_2_1 = list(btData_2_1.keys())
    # keys_1_2 = list(btData_1_2.keys())
    # keys_2_2 = list(btData_2_2.keys())
    # keys_1_3 = list(btData_1_3.keys())
    # keys_2_3 = list(btData_2_3.keys())

    data_list = []
    for i in keys_1_1:

        # ndarray(9999, 5)

        data_cur_min_1 = np.array((list(btData_1_1[i].values()))[3])
        data_cur_min_2 = np.array((list(btData_1_2[i].values()))[3])
        data_cur_min_3 = np.array((list(btData_1_3[i].values()))[3])
        data = np.vstack((data_cur_min_1, data_cur_min_2))
        data = np.vstack((data, data_cur_min_3))
        data_list.append(pd.DataFrame(data))

    return data_list







# way to read data_format1
# mean_data1 = []
# for i in keys_1_1:
#     data_cur_min = list(btData_1_1[i].values())
#     data = np.array(data_cur_min[3])
#     mean_data1_list = []
#     for d in range(data.shape[0]):
#         mean_data1_list.append(np.mean(data[d, 0:3]))
#     mean_data1.append(mean_data1_list)
# mean_data1 = np.array(mean_data1)
#
# mean_data2 = []
# for i in keys_1_2:
#     data_cur_min = list(btData_1_1[i].values())
#     data = np.array(data_cur_min[3])
#     mean_data1_list = []
#     for d in range(data.shape[0]):
#         mean_data1_list.append(np.mean(data[d, 0:3]))
#     mean_data2.append(mean_data1_list)
# mean_data2 = np.array(mean_data1)
#
# mean_data3 = []
# for i in keys_1_3:
#     data_cur_min = list(btData_1_1[i].values())
#     data = np.array(data_cur_min[3])
#     mean_data1_list = []
#     for d in range(data.shape[0]):
#         mean_data1_list.append(np.mean(data[d, 0:3]))
#     mean_data3.append(mean_data1_list)
# mean_data3 = np.array(mean_data1)
#
# for i in range(13):
#     mean_data1[i] = mean_data1[i] + mean_data2[i]
#     mean_data1[i] = mean_data1[i] + mean_data3[i]

# Now we get ndArray mean_data1, having 13 lists inside,
# each list contains the mean value.







