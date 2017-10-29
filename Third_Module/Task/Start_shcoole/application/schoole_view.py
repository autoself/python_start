#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-25 下午8:22'

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)



def run(object_city):
    shows_view = u'''
    \033[35;1m------- Schoole View --------\033[0m
    \033[32;1m1、创建课程
    2、创建班级
    3、创建老师
    4、创建学生
    5、查询课程
    6、查询班级
    7、查询老师
    8、查询学生
    9、返回
    10、退出
    \033[0m
    '''
    check_status = False
    while not check_status:
        print(shows_view)
        check_num = input('\033[34;1mPlease nums>>>>\033[0m')
        if check_num.isdigit():
            check_num = int(check_num)
            if check_num > 0 and check_num < 11:
                if check_num == 1:
                    name = input('课程名:').strip()
                    price = input('价格:').strip()
                    outline = input('周期:').strip()
                    check_status_obj = object_city.create_course(name,price,outline)
                    continue
                elif check_num == 2:
                    name = input('班级名:').strip()
                    course_name = input('课程名:').strip()
                    semester = input('学期:').strip()
                    check_status_obj = object_city.create_schoole_classe(name,course_name,semester)
                    continue
                elif check_num == 3:
                    numbers = input('老师编号:').strip()
                    name = input('老师名:').strip()
                    grade = input('职称:').strip()
                    school_class = input('任教班级(多个以逗号任开):').strip()
                    check_status_obj = object_city.create_teacher(numbers,name,grade,school_class)
                    continue
                elif check_num == 4:
                    numbers = input('学号>>').strip()
                    name = input('学生名>>').strip()
                    age = input('年龄>>').strip()
                    achievement = input('成绩>>').strip()
                    schoole_class = input('班级>>').strip()
                    check_status_obj = object_city.create_student(numbers,name,age,achievement,schoole_class)
                    continue
                elif check_num == 5:
                    name = input('课程名:').strip()
                    check_status_obj = object_city.get_course(name)
                    continue
                elif check_num == 6:
                    name = input('班级名:').strip()
                    check_status_obj = object_city.get_class(name)
                    continue
                elif check_num == 7:
                    name = input('老师名:').strip()
                    check_status_obj = object_city.get_teacher(name)
                    continue
                elif check_num == 8:
                    name = input('学生名:').strip()
                    check_status_obj = object_city.get_student(name)
                elif check_num == 9:
                    return False
                elif check_num == 10:
                    return True
            else:
                print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
