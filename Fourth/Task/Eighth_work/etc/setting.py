#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午9:50'

'''
主要存放一些基础的变量

高级FTP服务器开发：
1. 用户加密认证
2. 多用户同时登陆
3. 每个用户有自己的家目录且只能访问自己的家目录
4. 对用户进行磁盘配额、不同用户配额可不同
5. 用户可以登陆server后，可切换目录
6. 查看当前目录下文件
7. 上传下载文件，保证文件一致性
8. 传输过程中现实进度条
9. 支持断点续传

'''

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #基础目录
DB_DIR = os.path.join(BASEDIR,'db')        #数据库目录
USER_DIR = os.path.join(BASEDIR,'home')    #用户目录
DB_FILE = os.path.join(DB_DIR,'db.json')   #用户表
DB_PWD_MD5 = 'autoselfandylin'             #密码加密
#DOWNLOAD_DIR = os.path.join(BASEDIR,'download')

RED = '\033[31m'  # 红色
GREEN = '\033[32m'  # 绿色
YELLOW = '\033[33m'  # 黄色
BLUE = '\033[34m'  # 蓝色
FUCHSIA = '\033[35m'  # 紫红色
CYAN = '\033[36m'  # 青蓝色
WHITE = '\033[37m'  # 白色

#: no color
RESET = '\033[0m'  # 终端默认颜色