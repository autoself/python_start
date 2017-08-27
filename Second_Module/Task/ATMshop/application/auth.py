#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-24 下午8:52'


import time
import os
import json
from application import db_handle
from conf import setting

def access_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password:  credit account password
    :return:
    '''
    acc_path = db_handle.db_handle(setting.DATABASE)
    acc_file = os.path.join(acc_path,account+'.json')
    if os.path.isfile(acc_file):
        with open(acc_file,'r',encoding='utf-8') as pfile:
            account_data = json.load(pfile)
            if account_data['password'] == password:
                if account_data['status'] == 0:
                    export_time = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
                    if time.time() < export_time:
                        return account_data
                    else:
                        print("\033[31;1mThe card  %s is invalid!\033[0m" % account)
                else:
                    print("\033[31;1mUser %s disabled!\033[0m" % account)
            else:
                print("\033[31;1mAccount [%s] Password error!\033[0m" % account)
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)


def access_login(user_data,check_status,log_obj):
    '''
    account login func
    :param user_data: user info data , only save in memory
    :param log_obj:  logging login
    :return:
    '''
    retry_login_count = 0
    while user_data['is_auth'] is not True and retry_login_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        if check_status == 'ordinary':
            auth = access_auth(account,password)
        elif check_status == 'manger':
            auth = admin_auth(account, password)
        elif check_status == 'shopping':
            auth = shopping_auth(account, password)
        if auth:
            user_data['is_auth'] = True
            user_data['account_id'] = account
            return auth
        retry_login_count +=1


def admin_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password:  credit account password
    :return:
    '''
    acc_path = db_handle.db_handle(setting.DATABASE2)
    acc_file = os.path.join(acc_path,account+'.json')
    if os.path.isfile(acc_file):
        with open(acc_file,'r',encoding='utf-8') as pfile:
            account_data = json.load(pfile)
            if account_data['password'] == password:
                if account_data['status'] == 0:
                        return account_data
                else:
                    print("\033[31;1mUser %s disabled!\033[0m" % account)
            else:
                print("\033[31;1mAccount [%s] Password error!\033[0m" % account)
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)


def shopping_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password:  credit account password
    :return:
    '''
    acc_path = db_handle.db_handle(setting.DATABASE3)
    acc_file = os.path.join(acc_path,account+'.json')
    if os.path.isfile(acc_file):
        with open(acc_file,'r',encoding='utf-8') as pfile:
            account_data = json.load(pfile)
            if account_data['password'] == password:
                if account_data['status'] == 0:
                        return account_data
                else:
                    print("\033[31;1mUser %s disabled!\033[0m" % account)
            else:
                print("\033[31;1mAccount [%s] Password error!\033[0m" % account)
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)