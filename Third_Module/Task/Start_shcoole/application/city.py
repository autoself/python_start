#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-25 下午9:25'

import os
import sys
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from src.schoole import Schoole


def __select_db(city,getname):
    object_city = Schoole(city)
    if getname == 'create_course':
        name = input('课程名:').strip()
        price = input('价格:').strip()
        outline = input('周期:').strip()
        if not name or not price or not outline:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.create_course(name, price, outline)
        return check_status_obj
    elif getname == 'get_course':
        name = input('课程名:').strip()
        if not name:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.get_course(name)
        return  check_status_obj
    elif getname == 'create_class':
        name = input('班级名:').strip()
        course_name = input('课程名:').strip()
        teacher = input('讲师名:').strip()
        semester = input('学期:').strip()
        if not name or not course_name or not teacher or not semester:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.create_classe(name, course_name,teacher, semester)
        return check_status_obj
    elif getname == 'get_class':
        name = input('班级名:').strip()
        if not name:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.get_class(name)
        return check_status_obj
    elif getname == 'create_teacher':
        name = input('讲师名:').strip()
        if not name:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.create_teacher(name)
        return check_status_obj
    elif getname == 'get_teacher':
        name = input('讲师名:').strip()
        if not name:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.get_teacher(name)
        return check_status_obj
    elif getname == 'create_student':
        name = input('学生名>>')
        age = input('年龄>>')
        achievement = input('成绩>>')
        schoole_class = input('班级>>')
        if not name or not age or not achievement or not schoole_class:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.create_student(name,age,achievement,schoole_class)
        return check_status_obj
    elif getname == 'get_student':
        name = input('学生名>>')
        if not name:
            print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
            return False
        check_status_obj = object_city.get_student(name)
        return check_status_obj

def Cityrun(getname):
    shows_view = u'''
    \033[35;1m------- City View --------\033[0m
    '''
    check_status = False
    while not check_status:
        print(shows_view)
        schoole_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db','schoole.db')
        if not schoole_db:
            print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
            check_status = True
            continue
        with open(schoole_db,'rb') as fs:
            data = pickle.load(fs)
        if not data:
            print('\033[35;1m请选创建学校,感谢您的配合\033[0m')
            check_status = True
            continue
        for keys in data:
            print('    \033[32;1m%s、 %s \033[0m' % (keys,data[keys]['city']))
        _nums = len(data)
        print('    \033[32;1m%s、 %s \033[0m' % (_nums+1, '返回'))
        print('    \033[32;1m%s、 %s \033[0m' % (_nums + 2, '退出'))
        check_num = input('\033[34;1mPlease nums>>>>\033[0m')
        if check_num.isdigit():
            check_num = int(check_num)
            if check_num > 0 and check_num < len(data)+3:
                if check_num <= len(data):
                    check_status_obj = __select_db(data[check_num]['city'],getname)
                    continue
                elif check_num == _nums +1:
                    return False
                elif check_num == _nums + 2:
                    return True
                else:
                    print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')

