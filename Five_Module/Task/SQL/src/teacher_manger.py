#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-9 下午3:42'

import os
import sys

BASEHOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEHOME)

from etc import setting
from mode import model
from src import auth
from src.auth_login import user_data,auth_login


from sqlalchemy.orm import sessionmaker

@auth_login
def Show_Info():
    showinfo = u'''
    \033[35;1m------- Welcome Login in teacher manger system --------\033[0m
    \033[32;1m1、创建班级
    2、创建课程
    3、创建学员
    4、
    \033[0m
    '''


def run():
    user_auth = auth.access_login(user_data,'teacher')
    if user_auth:
        Show_Info()
