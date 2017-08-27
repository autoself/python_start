#!/usr/bin/env python
#-*- coding:utf-8 -*-


__author__ = 'andylin'
__date__ = '17-8-25 下午4:22'

from application.auth_login import auth_login

@auth_login
def inspect():
    '''
    Return and exit
    :return:
    '''
    menu_info = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1. 按任意键返回    2.退出
    \033[0m
    '''
    print(menu_info)
    option_num = input('Please select >>>').strip()
    if option_num == '2':
        return False
    else:
        return True