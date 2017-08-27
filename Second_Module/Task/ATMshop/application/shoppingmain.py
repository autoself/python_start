#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-27 下午5:00'

from application import auth
from application import auth_login
from application import logger
from application.auth_login import user_data
from application.auth_login import auth_login
from conf import setting
from application import db_handle
from application import shopping_atm
import os
import json

access_logger = logger.logger('shopping')

@auth_login
def Shopping(cart):
    sum_memory = 0
    for keys in cart:
        sum_memory = sum_memory + cart[keys]

    acc_carid = user_data['account_data']['card']
    cart_pass = input('Please card password >>>')
    check_status = shopping_atm.shopping_atm(acc_carid,cart_pass,sum_memory)
    if  check_status:
        print("\033[31;1m成功购买,感谢惠顾!\033[0m")
    else:

        return Coupling()







@auth_login
def Coupling():
    acc_path = db_handle.db_handle(setting.DATABASE4)
    acc_file = os.path.join(acc_path,'shop.db')
    with open(acc_file,'r',encoding='utf-8') as shopfiles:
        acc_dict = json.load(shopfiles)
    check_status = False
    shopping_cart = {}
    while not check_status:
        print("-------Shop---------")
        for key in acc_dict:
            for name in acc_dict[key]:
                print("%s.%s:%s" % (key,name,str(acc_dict[key][name])))
        select_num = input('Please select >>>')
        if select_num in acc_dict:
            if select_num == '5':
                print("\033[31;1m结账!\033[0m")
                check_status = True
            elif select_num == '6':
                print("\033[31;1mEnd shopping!\033[0m")
                return False
            else:
                for keys in acc_dict[select_num]:
                    print("\033[31;1m已添加入购物车%s!\033[0m" % (keys))
                    shopping_cart[keys] = acc_dict[select_num][keys]
        else:
            print("\033[31;1mThere is no such commodity!\033[0m")
    print("\033[31;1m总加入购物车%s!\033[0m" % (shopping_cart))
    Shopping(shopping_cart)
    return True


def run():
    '''
    this funciton will be shopping
    :return:
    '''
    acc_data = auth.access_login(user_data, 'shopping', access_logger)
    if user_data['is_auth']:
        access_logger.info('account_id %s login Success!' % (user_data['account_id']))
        user_data['account_data'] = acc_data
        Coupling()