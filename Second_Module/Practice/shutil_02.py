#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-16 下午10:00'

from shutil import copytree,rmtree
import logging
import os
path_dir = os.path.dirname(os.path.abspath(__file__))
def logs(messages):
    logger = logging.getLogger()
    sh = logging.FileHandler(os.path.join(path_dir,'test.log'))
    sF = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
    sh.setLevel(logging.WARNING)
    sh.setFormatter(sF)
    logger.addHandler(sh)
    logger.warning(messages)
    logger.removeHandler(sh)

def _logpath(path, names):
    logs("Working %s" % path)
    return ['1.txt']   # nothing will be ignored

def _logerr(*args):
    for i in args:
        logs("delete %s" % str(i))
    return ['a']
logs("start all")
#copytree('/data/test', '/data/test1',ignore=_logpath)
rmtree('/data/test2',ignore_errors=True,onerror=_logerr)


