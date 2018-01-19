#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午9:50'

'''
主要存放一些基础的变量
'''

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #基础目录
DB_DIR = os.path.join(BASEDIR,'db')        #数据库目录
USER_DIR = os.path.join(BASEDIR,'home')    #用户目录
DB_FILE = os.path.join(DB_DIR,'db.json')   #用户表
DB_PWD_MD5 = 'autoselfandylin'             #密码加密

RED = '\033[31m'  # 红色
GREEN = '\033[32m'  # 绿色
YELLOW = '\033[33m'  # 黄色
BLUE = '\033[34m'  # 蓝色
FUCHSIA = '\033[35m'  # 紫红色
CYAN = '\033[36m'  # 青蓝色
WHITE = '\033[37m'  # 白色

#: no color
RESET = '\033[0m'  # 终端默认颜色