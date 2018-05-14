#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-10 下午1:51'

import os
import sys

BASEHOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEHOME)

from src import teacher_manger
from src import student_manger


def run():
    info =u'''
    \033[35;1m------- All View --------\033[0m
    \033[32;1m1、老师
    2、学员
    3、退出
    \033[0m
    '''
    check_all_view_status = False
    while not check_all_view_status:
        print(info)
        select_all_view_nums =  input('\033[34;1mPlease nums>>>>\033[0m')
        if select_all_view_nums.isdigit():
            if select_all_view_nums == '1':
                status = teacher_manger.run()
                if not status:
                    check_all_view_status = True
                    print('\033[36;1m欢迎下次光临,再见!\033[0m')
            elif select_all_view_nums == '2':
                status = student_manger.run()
                if not status:
                    check_all_view_status = True
                    print('\033[36;1m欢迎下次光临,再见!\033[0m')
            elif select_all_view_nums == '3':
                print('\033[36;1m欢迎下次光临,再见!\033[0m')
                check_all_view_status = True
            else:
                print('\033[33;1m请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m请选择正确的选项，感谢你的合作!\033[0m')

