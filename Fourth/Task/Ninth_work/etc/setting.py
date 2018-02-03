#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-24 下午2:43'


'''
类 Fabric 主机管理程序开发：
1. 运行程序列出主机组或者主机列表
2. 选择指定主机或主机组
3. 选择让主机或者主机组执行命令或者向其传输文件（上传/下载）
4. 充分使用多线程或多进程
5. 不同主机的用户名密码、端口可以不同




'''

import os
import logging

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 基础目录
DB_DIR = os.path.join(BASEDIR,'db')                                    #代表为数据库
DB_USER = os.path.join(DB_DIR,'user.json')                             #用户数据表
DB_GROUP = os.path.join(DB_DIR,'group.json')                           #用户组数据表


#Log correlation type
LOG_ACTIVE = 'ON'
LOG_LEVEL = logging.INFO
LOG_PATH = os.path.join(BASEDIR,'logs')
LOG_TYPES = {
    'access':'access.log',
    'error': 'error.log',
}


RED = '\033[31m'  # 红色
GREEN = '\033[32m'  # 绿色
YELLOW = '\033[33m'  # 黄色
BLUE = '\033[34m'  # 蓝色
FUCHSIA = '\033[35m'  # 紫红色
CYAN = '\033[36m'  # 青蓝色
WHITE = '\033[37m'  # 白色

#: no color
RESET = '\033[0m'  # 终端默认颜色
