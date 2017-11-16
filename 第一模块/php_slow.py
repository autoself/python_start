#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-11-16 下午9:46'


import logging
from logging import handlers
import  os, datetime
import subprocess


def phplog(status,loglevel,logdir='/data/logs/scriptlog/phpslow'):
    if not os.path.isdir(logdir):
        os.makedirs(logdir)
    logger = logging.getLogger(status)
    logger.setLevel(loglevel)
    logfile = os.path.join(logdir,'php.log')
    logbackfile = handlers.RotatingFileHandler(filename=logfile, maxBytes=5120, backupCount=3, encoding='utf-8')
    logfomater = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
    logbackfile.setLevel(loglevel)
    logbackfile.setFormatter(logfomater)
    logger.addHandler(logbackfile)
    return logger


class PhpCheck(object):

    def __init__(self,logger,phpfile='/data/logs/php/php-slow.log'):

        self.phpfile = phpfile
        self.logger = logger

    def mvfile(self):
        otherday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
        if not os.path.isfile(self.phpfile):
            self.logger.error('日志文件不存在!请检查')
            return False
        backfile = os.path.join('aa', self.phpfile + '.' + otherday)
        checkstatus = subprocess.call(['mv', self.phpfile, backfile])
        if checkstatus != 0:
            self.logger.error('迁移文件失败!')
            return False

if __name__ == '__main__':
    logger = phplog('access',logging.DEBUG)
    checkLog = PhpCheck(logger)
    checkLog.mvfile()
