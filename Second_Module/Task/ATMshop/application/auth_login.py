#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-25 下午10:22'


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_auth':False,
    'account_data':None
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