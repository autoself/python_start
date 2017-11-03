#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-25 下午8:22'

import os
import sys
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.schoole import BaseSchoole
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
    \033[35;1m------- Schoole View --------\033[0m
    \033[32;1m1、创建学校
    2、创建课程
    3、创建班级
    4、创建讲师
    5、创建学生
    6、查询课程
    7、查询班级
    8、查询讲师
    9、查询学生
    10、查询学校
    11、返回
    12、退出
    \033[0m
    '''
    check_status = False
    while not check_status:
        print(shows_view)
        check_num = input('\033[34;1mPlease nums>>>>\033[0m')
        if check_num.isdigit():
            check_num = int(check_num)
            if check_num > 0 and check_num < 13:
                if check_num == 1:
                    name = input('学校名称>>').strip()
                    addr = input('学校地址>>').strip()
                    city = input('区域>>').strip()
                    if not name or not addr or not city :
                        print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
                        continue
                    obj = BaseSchoole(name,addr,city)
                    check_status_obj = obj.create_schoole()
                    if check_status_obj:
                        print('\033[35;1m创建%s校区成功!\033[0m' % (city))
                    else:
                        print('\033[35;1m创建%s校区失败!\033[0m' % (city))
                    continue
                elif check_num == 2:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj =  Cityrun('create_course')
                    if obj:
                        return True
                    continue
                elif check_num == 3:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('create_class')
                    if obj:
                        return True
                    continue
                elif check_num == 4:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('create_teacher')
                    if obj:
                        return True
                    continue
                elif check_num == 5:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('create_student')
                    if obj:
                        return True
                    continue
                elif check_num == 6:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('get_course')
                    if obj:
                        return True
                    continue
                elif check_num == 7:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('get_class')
                    if obj:
                        return True
                    continue
                elif check_num == 8:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('get_teacher')
                    if obj:
                        return True
                    continue
                elif check_num == 9:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    obj = Cityrun('get_student')
                    if obj:
                        return True
                    continue
                elif check_num == 10:
                    check_schoole_db =  __check_schoole()
                    if not check_schoole_db:
                        print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
                    continue
                elif check_num == 11:
                    return False
                elif check_num == 12:
                    return True
            else:
                print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')