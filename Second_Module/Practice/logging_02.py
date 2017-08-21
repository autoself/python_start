#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-12 下午9:26'


import os
import logging



logger = logging.getLogger('TETST-lOG')
logger.setLevel(logging.DEBUG)


ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

fh = logging.FileHandler('access.log'.encode(encoding='utf-8'))
fh.setLevel(logging.ERROR)

ff = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
cf = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
ch.setFormatter(cf)
fh.setFormatter(ff)


logger.addHandler(fh)
logger.addHandler(ch)


logger.warning('warning happing ... ')
logger.error('error happing....')
