#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-27 下午7:37'


import os
import json
from conf import setting
from application import db_handle
from application import db_log

def shopping_atm(accout_id,password,memory):
    acc_path = db_handle.db_handle(setting.DATABASE)
    acc_file = os.path.join(acc_path, str(accout_id) +'.json')
    if os.path.isfile(acc_file):
        with open(acc_file,'r',encoding='utf-8') as cardfile:
            card_dict = json.load(cardfile)
        if card_dict['password'] == password:
            if card_dict['status'] == 0:
                if card_dict['balance'] > memory:
                    card_dict['balance'] = round(card_dict['balance'] - memory,2)
                    with open(acc_file,'w',encoding='utf-8') as newfile:
                        json.dump(card_dict,newfile)
                    db_log.atmlog(str(accout_id), '购物消费:%s' % (str(memory)))
                    return True
    return False
