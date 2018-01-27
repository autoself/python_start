#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-26 下午4:38'




import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from etc import setting






def __rds_database():
    if os.path.isdir(setting.DB_DIR):
        if os.path.isfile(setting.DB_FILE):
            try:
                with open(setting.DB_FILE, 'r', encoding='utf-8') as fr:
                    data = json.load(fr)
            except IOError:
                raise "System Error is not  read file! "
            finally:
                return data
    else:
        os.makedirs(setting.DB_DIR)
        data = 0
        return data



def add_machine():





def run():
    info='''
    \033[35;1m------- USER View --------\033[0m
    \033[32;1m请选择:
    1、查看所有的组
	2、查看某台服务器信息
	3、修改某台服务器信息
	4、添加新服务器信息
	5、删除服务器信息
	6、删除组所有服务器
	7、退出
    \033[0m
    '''
    print(info)




run()
