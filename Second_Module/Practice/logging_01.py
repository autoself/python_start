#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-12 下午4:22'


import logging
import os

path_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(path_dir,'app.log')
logging.basicConfig( filename= log_file,level=logging.WARNING, format='%(asctime)s %(levelname)s  %(filename)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )

logging.debug('check Debug')
logging.warning('check warning')