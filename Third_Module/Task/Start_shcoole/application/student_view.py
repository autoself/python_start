#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-11-10 下午4:15'


import os
import sys
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from application.city import Cityrun

def __check_schoole():
    db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db','schoole.db')
    if os.path.isfile(db):
        with open(db,'rb') as fs:
            data = pickle.load(fs)
        if data:
            return True
    return False

def run():
    shows_view = u'''
    \033[35;1m------- Student View --------\033[0m
    \033[32;1m1、注册学员
    2、交学费
	3、学员成绩查询
    4、返回
    5、退出
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
                    check_schoole_db = __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('create_s_student')
                    if obj:
                        return True
                    continue
                elif check_num == 2:
                    check_schoole_db = __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('jiao_student')
                    if obj:
                        return True
                    continue
                elif check_num == 3:
                    check_schoole_db = __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('get_student')
                    if obj:
                        return True
                    continue
                elif check_num == 4:
                    return False
                elif check_num == 5:
                    return True
            else:
                print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')