#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-26 上午9:25'

import os
import json
from application import db_handle
from conf import setting


def updatememory(account,opt,field,accvalue):
    acc_path = db_handle.db_handle(setting.DATABASE)
    acc_file = os.path.join(acc_path, account + '.json')
    with open(acc_file,'r',encoding='utf-8') as oldfile:
        olddata = json.load(oldfile)
    if opt == 'repay':
        olddata[field] = round(olddata[field] + accvalue,2)
    elif opt == 'withdraw':
        olddata[field] =  olddata[field] - accvalue - round(accvalue * 0.05,2)
        if olddata[field] < 0:
            return False
    with open(acc_file,'w',encoding='utf-8') as newfile:
        json.dump(olddata,newfile)
    return olddata



def updatecard(account,field,accvalue):
    acc_path = db_handle.db_handle(setting.DATABASE)
    acc_file = os.path.join(acc_path, account + '.json')
    with open(acc_file,'r',encoding='utf-8') as oldfile:
        olddata = json.load(oldfile)
    olddata[field] =  accvalue
    with open(acc_file,'w',encoding='utf-8') as newfile:
        json.dump(olddata,newfile)
    return True