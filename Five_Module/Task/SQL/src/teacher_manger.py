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
    4、创建上课记录
    5、显示管理的班级
    6、修改学生成绩
    7、返回
    8、退出
    \033[0m
    '''
    check_teacher_status = False
    while not check_teacher_status:
        print(showinfo)
        select_all_view_nums = input('\033[34;1mPlease nums>>>>\033[0m')
        if select_all_view_nums.isdigit():
            if select_all_view_nums == '1':
                pass
            elif select_all_view_nums == '2':
                pass
            elif select_all_view_nums == '3':
                pass
            elif select_all_view_nums == '4':
                pass
            elif select_all_view_nums == '5':
                pass
            elif select_all_view_nums == '6':
                pass
            elif select_all_view_nums == '7':
                user_data['is_auth'] = False
                return True
            elif select_all_view_nums == '8':
                return False
        else:
            print('\033[33;1m请选择正确的选项，感谢你的合作!\033[0m')

def run():
    user_auth = auth.access_login(user_data,'teacher')
    if user_auth:
        #status = Show_Info()
        return Show_Info()
