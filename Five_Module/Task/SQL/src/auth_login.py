#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-11 下午4:05'


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_auth':False,
    'username':None
}

def auth_login(func):
    '''
    author Decorator
    :return:
    '''
    def login(*args,**kwargs):
        if user_data['is_auth']:
            return func(*args,**kwargs)
        else:
            return False
    return login