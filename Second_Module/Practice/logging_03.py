#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-12 下午10:14'


import logging
def logs(messages):
    logger = logging.getLogger()
    handler = logging.FileHandler('access.log')
    fileFamter = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
    handler.setFormatter(fileFamter)
    handler.setLevel(logging.WARNING)
    logger.addHandler(handler)

    shandle = logging.StreamHandler()
    shandle.setFormatter(fileFamter)
    shandle.setLevel(logging.WARNING)
    logger.addHandler(shandle)

    logger.warning(messages)
    logger.removeHandler(handler)
    logger.removeHandler(shandle)

nowstr = "waring happing ..."
logs(nowstr)