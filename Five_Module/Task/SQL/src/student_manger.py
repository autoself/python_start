#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-10 下午2:25'


from src import auth
from src.auth_login import user_data,auth_login



@auth_login
def put_work():
    pass

@auth_login
def show_work_task():
    pass

@auth_login
def show_self_solt():
    pass

@auth_login
def Show_Info():
    showinfo = '''
    \033[35;1m------- Welcome Login in student manger system --------\033[0m
    \033[32;1m1、提交作业
    2、查看作业成绩
    3、查看自已成绩的排名
    4、返回
    5、退出
    \033[0m  
    '''
    check_student_status = False
    while not check_student_status:
        print(showinfo)
        select_all_view_nums = input('\033[34;1mPlease nums>>>>\033[0m')
        if select_all_view_nums.isdigit():
            if select_all_view_nums == '1':
                put_work()
            elif select_all_view_nums == '2':
                show_work_task()
            elif select_all_view_nums == '3':
                show_self_solt()
            elif select_all_view_nums == '4':
                user_data['is_auth'] = False
                return True
            elif select_all_view_nums == '5':
                return False
        else:
            print('\033[33;1m请选择正确的选项，感谢你的合作!\033[0m')
    
def run():
    user_auth = auth.access_login(user_data,'student')
    if user_auth:
        #status = Show_Info()
        return Show_Info()
