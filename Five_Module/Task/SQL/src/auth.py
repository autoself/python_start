#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-11 下午4:02'


import os
import sys

BASEHOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEHOME)

from etc import setting
from sqlalchemy.orm import sessionmaker
from mode import model
import time


def access_t_auth(username,password):
    Session_class = sessionmaker(bind=setting.engine)
    Session = Session_class()
    data = Session.query(model.Teacher).filter_by(name=username).first()
    if data:
        if data.password == password:
            data.login_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            Session.commit()
            Session.close()
            return True
    return False



def access_s_auth(username, password):
    pass

def access_login(user_data,selectname):
    retry_login_count = 0
    while user_data['is_auth'] is not True and retry_login_count < 3:
        username = input("\033[32;1musername:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        if selectname == 'teacher':
            auth = access_t_auth(username, password)
        else:
            auth = access_s_auth(username,password)
        if auth:
            user_data['is_auth'] = True
            user_data['username'] = username
            return auth
        retry_login_count += 1