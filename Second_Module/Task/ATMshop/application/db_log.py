#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-26 下午8:16'

import os
import time
from conf import setting

def atmlog(account,messages):
    '''
     bill funcs
    :param account:
    :param messages:
    :return:
    '''
    acc_file = os.path.join(setting.BASE_DIR,'db','history',account+'.db')
    dtime = time.strftime("%Y-%m-d %H:%M:%S",time.localtime(time.time()))
    with open(acc_file,'a+',encoding='utf-8') as acc:
        acc.write('%s -- %s\n' % (dtime,messages))
    return True

