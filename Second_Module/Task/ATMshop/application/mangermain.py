#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-26 下午9:28'


from application import auth
from application import logger
from application.auth_login import user_data
from application.auth_login import auth_login
from conf import setting
from application import db_handle
from application import countmoney
import time
import os
import json

access_logger = logger.logger('admin')



@auth_login
def New_Card():
    '''
    new card func
    :return:
    '''
    access_logger.info('account_id %s option new card!' % (user_data['account_id']))
    newcard = input('Please new card >>>>').strip()
    if newcard.isdigit():
        acc_path = db_handle.db_handle(setting.DATABASE)
        acc_file = os.path.join(acc_path,newcard+'.json')
        list_db = os.listdir(acc_path)
        list_now = [i.replace('.json', '') for i in list_db ]
        if newcard not in list_now:
            now_data = setting.NEW_CARDS
            now_data['id'] = newcard
            now_data['enroll_date'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            with open(acc_file,'w',encoding='utf-8') as newfile:
                json.dump(now_data,newfile)
        else:
            print("\033[31;1m Card already exists!\033[0m")

    else:
        print("\033[31;1m Incorrect input of card number!\033[0m")
    return True

@auth_login
def Modify_quota():
    access_logger.info('account_id %s option Modify_quota!' % (user_data['account_id']))
    change_status = False
    check_num = 0
    while not change_status:
        cardnum = input('Please card >>>')
        if cardnum.isdigit():
            acc_path = db_handle.db_handle(setting.DATABASE)
            list_db = os.listdir(acc_path)
        list_now = [i.replace('.json', '') for i in list_db]
        if cardnum in list_now:
            cardepoll = input('Please credit >>>')
            if cardepoll.isdigit():
                if  int(cardepoll) > 15000:
                    countmoney.updatecard(cardnum,'credit',cardepoll)
                    change_status = True
        if check_num == 2:
            change_status =True
        check_num += 1
    return True


@auth_login
def Frozen():
    access_logger.info('account_id %s option Frozen!' % (user_data['account_id']))
    change_status = False
    check_num = 0
    while not change_status:
        cardnum = input('Please card >>>')
        if cardnum.isdigit():
            acc_path = db_handle.db_handle(setting.DATABASE)
            list_db = os.listdir(acc_path)
        list_now = [i.replace('.json', '') for i in list_db]
        if cardnum in list_now:
            cardepoll = input('Please status >>>')
            if cardepoll.isdigit():
                if int(cardepoll) == 1:
                    countmoney.updatecard(cardnum, 'status', int(cardepoll))
                    change_status = True
        if check_num == 2:
            change_status = True
        check_num += 1
    return True



@auth_login
def Loginout():
    access_logger.info('account_id %s option Exited!' % ( user_data['account_id']))
    return False

@auth_login
def Coupling():
    '''
    ATM display function
    :param acc_data: Related cache
    :return:
    '''
    shows_open = u'''
     ------- Oldboy Bank ---------
    \033[32;1m1. 新开户
    2. 调整用户额度
    3. 冻结账户
    4. 退出
    \033[0m
    '''
    shows_dic = {
        '1': 'New_Card()',
        '2': 'Modify_quota()',
        '3': 'Frozen()',
        '4': 'Loginout()'
    }
    check_status = True
    while check_status:
        print(shows_open)
        options = input('Please select >>>').strip()
        if options in shows_dic:
            check_status = eval(shows_dic[options])
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    '''
    this funciton will be called right a way when the program started
    :return:
    '''
    acc_data = auth.access_login(user_data, 'manger', access_logger)
    if user_data['is_auth']:
        access_logger.info('account_id %s login Success!' % (user_data['account_id']))
        user_data['account_data'] = acc_data
        Coupling()