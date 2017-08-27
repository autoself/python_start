#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-24 下午8:51'

'''
ATM Operation record
'''

import logging
import os
from conf import setting


def logger(log_type):
    '''
    Logging function
    :param log_type: Log type
    :return:
    '''
    if setting.LOG_ACTIVE == 'OFF':
        return
    #create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)

    #create file handler and set level
    logfile = os.path.join(setting.LOG_PATH,setting.LOG_TYPES[log_type])
    fileha = logging.FileHandler(logfile)
    fileha.setLevel(setting.LOG_LEVEL)

    #create formaster
    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #add formaster to handler
    fileha.setFormatter(formater)

    #add logger handler
    logger.addHandler(fileha)

    return logger
