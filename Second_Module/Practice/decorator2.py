#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-1 下午9:57'


uname = "andylin"
passwd = "abc123"

def auth(auto_type):
    def login_check(func):
        def login(*args,**kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()
            if username == uname and passwd == password:
                if auto_type == 'job':
                    func(*args,**kwargs)
                    print("Authentication Success! Welcome to job!")
                elif auto_type == 'home':
                    func(*args,**kwargs)
                    print('Authentication Success!Welcome to home!')
                else:
                    func(*args, **kwargs)
                    print('Authentication Success!Welcome to shcool!')
            else:
                print("Authentication Faild!")
        return login
    return  login_check


@auth(auto_type='job')
def job():
    print("login Welcome to job!")

@auth(auto_type='home')
def home():
    print("login Welcome to home!")

@auth(auto_type='school')
def school():
    print("login Welcome to school!")



job()
home()
school()