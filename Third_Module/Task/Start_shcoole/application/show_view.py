#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-25 下午9:39'

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from application import schoole_view
from application import student_view
from application import teacher_view
def run():
    shows_view = u'''
    \033[35;1m------- City View --------\033[0m
    \033[32;1m1、学校视图
    2、老师视图
    3、学生视图
    4、退出
    \033[0m
    '''
    check_status = False
    while not check_status:
        print(shows_view)
        check_num = input('\033[34;1mPlease nums>>>>\033[0m')
        if check_num.isdigit():
            check_num = int(check_num)
            if check_num > 0 and check_num < 6:
                if check_num == 1:
                    check_status = schoole_view.run()
                    if check_status:
                        check_status = True
                elif check_num == 2:
                    check_status = teacher_view.Cityrun()
                elif check_num == 3:
                    check_status = student_view.run()
                    if check_status:
                        check_status = True
                elif check_num == 4:
                    return False
                elif check_num == 5:
                    return True
            else:
                print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
