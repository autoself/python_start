#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-9 下午8:50'


import time




time_stamp = time.time()

local_time = time.localtime()

timestamp_change_local = time.localtime(time_stamp)
print(timestamp_change_local)

local_change_timestamp = time.mktime(local_time)
print(local_change_timestamp )

local_change_string = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(local_change_string)

string_change_local = time.strptime("2017-08-09 20:55:30",'%Y-%m-%d %H:%M:%S')
print(string_change_local)