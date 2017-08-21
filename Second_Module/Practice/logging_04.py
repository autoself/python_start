#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-12 下午10:44'



import logging
from logging import handlers

logger = logging.getLogger('Test')

log_file = 'timelog.log'

#fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3,encoding='utf-8')
fh = handlers.TimedRotatingFileHandler(filename=log_file,when='D',interval=7,backupCount=7)

logfm = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')

fh.setFormatter(logfm)
fh.setLevel(logging.WARNING)
logger.addHandler(fh)

logger.warning('test1')
logger.warning('test2')
logger.warning('test3')
logger.warning('test4')