#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-11-12 上午9:09'



import os
import sys
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from src.schoole import Schoole


def __check_teacher_login(city):
    db_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db',city, 'teacher.db')
    if db_data:
        useranme = input('讲师名>>>').strip()
        password = input('密码>>>').strip()
        with open(db_data, 'rb') as fr:
            db = pickle.load(fr)
        for key in db:
            if useranme == db[key]['name'] and password == db[key]['password']:
                return useranme
        else:
            print('\033[33;1m 讲师的账号或密码错误!\033[0m')
    else:
        print('\033[33;1m 还没有讲师,请联系管理人员!\033[0m')
        return False



def Cityrun():
    shows_view = u'''
    \033[35;1m------- Teacher View --------\033[0m
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
                    check_status_obj = __check_teacher_login(data[check_num]['city'])
                    if check_status_obj:
                        run(data[check_num]['city'],check_status_obj)
                    continue
                elif check_num == _nums +1:
                    return False
                elif check_num == _nums + 2:
                    return True
                else:
                    print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')


def run(city,name):
    shows_view = u'''
    \033[35;1m------- Teacher View --------\033[0m
    \033[32;1m1、查看班级学员列表
    2、修改学员的成绩
	3、返回
    4、退出
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
                    class_data = input('请输入班级>>>').strip()
                    if not class_data:
                        print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
                    else:
                        obj = Schoole(city)
                        check_status_obj = obj.get_teacher_student(name,class_data)
                    continue
                elif check_num == 2:
                    class_data = input('请输入班级>>>').strip()
                    student_data = input('请输入学员>>>').strip()
                    achievement_data = input('请输入成绩>>>').strip()
                    if not class_data or not student_data or not achievement_data:
                        print('\033[35;1m请把所有参数输入完整,感谢您的合作!\033[0m')
                    else:
                        obj = Schoole(city)
                        check_status_obj = obj.change_teacher_course(name, class_data,student_data,achievement_data)
                    continue
                elif check_num == 3:
                    return False
                elif check_num == 4:
                    return True
            else:
                print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')
        else:
            print('\033[33;1m 请选择正确的选项，感谢你的合作!\033[0m')