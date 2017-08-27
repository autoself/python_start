#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-24 下午8:44'


import logging
from application import auth
from application import logger
from application.inspect import inspect
from application.auth_login import user_data
from application.auth_login import auth_login
from application import countmoney
from conf import setting
from application import db_handle
from application import db_log
import os

#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


@auth_login
def Account_info():
    access_logger.info('account_id %s option account_info' % (user_data['account_id']))
    user_info = u'''
    ------- Oldboy Bank ---------
    \033[34;1m
    卡号:%s
    余额:%s
    额度:%s
    有效期:%s
    \033[0m
    '''  % ( user_data['account_id'],user_data['account_data']['balance'],user_data['account_data']['credit'], user_data['account_data']['expire_date'])
    print(user_info)
    return inspect()

@auth_login
def Repay():
    access_logger.info('account_id %s option Repay' % ( user_data['account_id']))
    user_info = u'''
    ------- Oldboy Bank ---------
    \033[34;1m
    卡号:%s
    余额:%s
    额度:%s
    \033[0m
    '''  % ( user_data['account_id'], user_data['account_data']['balance'], user_data['account_data']['credit'])
    print(user_info)
    check_status = False
    check_num = 0
    while not check_status:
        repay_memory = input('Please memory >>>').strip()
        if repay_memory.isdigit():
            if int(repay_memory)%100 == 0:
                check_status = True
        if check_num == 2:
            return False
        check_num +=1
    nowacc_data = countmoney.updatememory(user_data['account_id'],'repay','balance',int(repay_memory))
    if nowacc_data:
        user_data['account_data'] = nowacc_data
        access_logger.info('account_id %s option Repay memory: %s' % (user_data['account_id'],str(repay_memory)))
        db_log.atmlog(user_data['account_id'],'ATM存入%s' % (str(repay_memory)))
        return inspect()


@auth_login
def Withdraw():
    access_logger.info('account_id %s option Withdraw' % (user_data['account_id']))
    user_info = u'''
        ------- Oldboy Bank ---------
        \033[34;1m
        卡号:%s
        余额:%s
        额度:%s
        \033[0m
        ''' % (user_data['account_id'], user_data['account_data']['balance'], user_data['account_data']['credit'])
    print(user_info)
    check_status = False
    check_num = 0
    while not check_status:
        repay_memory = input('Please memory >>>').strip()
        if repay_memory.isdigit():
            if int(repay_memory) % 100 == 0:
                check_status = True
        if check_num == 2:
            return False
        check_num += 1
    nowacc_data = countmoney.updatememory(user_data['account_id'], 'withdraw','balance', int(repay_memory))
    if nowacc_data:
        user_data['account_data'] = nowacc_data
        access_logger.info('account_id %s option Repay memory: %s' % (user_data['account_id'], str(repay_memory)))
        db_log.atmlog(user_data['account_id'],'ATM取出%s' % (str(repay_memory)))
    else:
        print("\033[31;1m Withdrawals failed, not so much money!\033[0m")
    return inspect()

@auth_login
def Transfer():
    access_logger.info('account_id %s option Transfer' % (user_data['account_id']))
    user_info = u'''
            ------- Oldboy Bank ---------
            \033[34;1m
            卡号:%s
            余额:%s
            额度:%s
            \033[0m
            ''' % (user_data['account_id'], user_data['account_data']['balance'], user_data['account_data']['credit'])
    print(user_info)
    check_status = False
    check_num = 0
    while not check_status:
        other_numbers = input('Please other account_id >>>>')
        if other_numbers.isdigit():
            if other_numbers != user_data['account_id']:
                acc_path = db_handle.db_handle(setting.DATABASE)
                list_db = os.listdir(acc_path)
                list_now = [ i.replace('.json','') for i in list_db if i.replace('.json','') != user_data['account_id'] ]
                if other_numbers in list_now:
                    memory = input("Please memory >>>")
                    if memory.isdigit():
                        nowacc_data = countmoney.updatememory(user_data['account_id'], 'withdraw', 'balance', int(memory))
                        if not nowacc_data:
                            print("\033[31;1m Withdrawals failed, not so much money!\033[0m")
                        else:
                            db_log.atmlog(user_data['account_id'],'ATM转出:%s 卡号:%s' % (str(memory),other_numbers))
                            countmoney.updatememory(other_numbers, 'repay', 'balance',int(memory))
                            db_log.atmlog(other_numbers,'ATM转入:%s 卡号:%s' % (str(memory),user_data['account_id']))
                            user_data['account_data'] = nowacc_data
                            check_status = True
                else:
                    print("\033[31;1m The input account does not exist!\033[0m")
            else:
                print("\033[31;1m Enter an account not yourself!\033[0m")
        if check_num == 2:
            return False
        check_num += 1
    return inspect()

@auth_login
def Bill():
    access_logger.info('account_id %s option Bill' % (user_data['account_id']))
    bill_dir = os.path.join(setting.BASE_DIR,'db','history')
    biil_file = os.path.join(bill_dir,user_data['account_id']+'.db')
    if os.path.isfile(biil_file):
        with open(biil_file,'r',encoding='utf-8') as openfile:
            for line in openfile:
                print(line.replace('\n',''))
    else:
        print("\033[31;1m New card, the repayment of consumption!\033[0m")
    return inspect()


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
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m
    '''
    shows_dic = {
        '1': 'Account_info()',
        '2': 'Repay()',
        '3': 'Withdraw()',
        '4': 'Transfer()',
        '5': 'Bill()',
        '6': 'Loginout()'
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
    acc_data = auth.access_login( user_data,'ordinary',access_logger)
    if user_data['is_auth']:
        access_logger.info('account_id %s login Success!' % ( user_data['account_id']))
        user_data['account_data'] = acc_data
        Coupling()