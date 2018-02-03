#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-27 下午2:49'

'''
回顾学习(遗忘不可耻,可耻不温习):

python 使用 logging 模块记录日志涉及四个主要类，使用官方文档中的概括最为合适:
  logger提供了应用程序可以直接使用的接口;
  handler将(logger创建的)日志记录发送到合适的目的输出;
  filter提供了细度设备来决定输出哪条日志记录；
  formatter决定日志记录的最终输出格式.

logger 每个程序在输出信息之前获得一个logger. logger通常对应了程序的模块名，比如聊天工具的图形界面模块可以这样获得它的logger

LOG = logging.getLogger("chat.gui")

Logger.setLevel(lel): 指定最低的日志级别，低于lel的级别将被忽略. debug是最低的内置级别，critical为最高
Logger.addFilter(filt) , Logger.removerFilter(filt);  添加或删除指定的filter
'''

import logging
from etc import setting
import os


def logger(log_type):

    # create console handler and set level to level
    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)

    #screen display
    #logshow = logging.StreamHandler()
    #logshow.setLevel(setting.LOG_LEVEL)


    # create log directory
    if not os.path.isdir(setting.LOG_PATH):
        os.makedirs(setting.LOG_PATH)
    #log file position
    logfile = os.path.join(setting.LOG_PATH,setting.LOG_TYPES[log_type])

    #create file handler, and set level
    fh = logging.FileHandler(logfile)
    fh.setLevel(setting.LOG_LEVEL)

    #create format
    formater = logging.Formatter("%(asctime)s %(levelname)s  %(message)s")

    #file handler setting formater
    fh.setFormatter(formater)

    # addr logger handler
    logger.addHandler(fh)
    #logger.addHandler(logshow)

    return logger
