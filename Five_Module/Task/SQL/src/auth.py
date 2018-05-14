#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-11 下午4:02'


import os
import sys

BASEHOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEHOME)

from src.model_session import session_db

from mode import model
import time


def access_auth(dbtable,username,password):
    Session = session_db()
    data = Session.query(dbtable).filter_by(name=username).first()
    if data:
        if data.password == password:
            data.login_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            Session.commit()
            Session.close()
            return True
    return False



def access_login(user_data,selectname):
    retry_login_count = 0
    while user_data['is_auth'] is not True and retry_login_count < 3:
        username = input("\033[32;1musername:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        if username and password:
            if selectname == 'teacher':
                auth = access_auth(model.Teacher,username, password)
            else:
                auth = access_auth(model.Student,username,password)
            if auth:
                user_data['is_auth'] = True
                user_data['username'] = username
                return auth
        print('\033[36;1m请输入正确的用户名和密码!\033[0m')
        retry_login_count += 1
