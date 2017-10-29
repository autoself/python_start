#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-25 下午9:25'

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from src.schoole import Schoole
from  application import show_view


def run():
    shows_view = u'''
    \033[35;1m------- City View --------\033[0m
    \033[32;1m1、选择北京校区
    2、选择上海校区
    3、退出
    \033[0m
    '''
    check_status = False
    while not check_status:
        print(shows_view)
        check_num = input('\033[34;1mPlease nums>>>>\033[0m')
        if check_num.isdigit():
            check_num = int(check_num)
            if check_num > 0 and check_num < 5:
                if check_num == 1:
                    object_schoole = Schoole('依林大学院校', '北京是环市东路1号', 'BeiJing')
                    db_dir = os.path.join(BASE_DIR,'db','BeiJing')
                    if not os.path.isdir(db_dir):
                        os.makedirs(db_dir)
                    check_status = show_view.run(object_schoole)
                    if check_status:
                        return True
                elif check_num == 2:
                    object_schoole = Schoole('依林上海分校', '上海是浦东东路1号', 'Shanghai')
                    db_dir = os.path.join(BASE_DIR, 'db', 'Shanghai')
                    if not os.path.isdir(db_dir):
                        os.makedirs(db_dir)
                    check_status = show_view.run(object_schoole)
                    continue
                elif check_num == 3:
                    return True
                else:
                    print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
