#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-24 下午9:27'


import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}

DATABASE2 = {
    'engine': 'file_storage',
    'name': 'admin',
    'path': "%s/db" % BASE_DIR
}

DATABASE3 = {
    'engine': 'file_storage',
    'name': 'shopping',
    'path': "%s/db" % BASE_DIR
}


DATABASE4 = {
    'engine': 'file_storage',
    'name': 'Shop',
    'path': "%s/db" % BASE_DIR
}

#Log correlation type
LOG_ACTIVE = 'ON'
LOG_LEVEL = logging.INFO
LOG_PATH = os.path.join(BASE_DIR,'logs')
LOG_TYPES = {
    'transaction':'transaction.log',
    'access':'access.log',
    'admin': 'admin.log',
    'shopping': 'shopping.log'
}

NEW_CARDS = {
    "status": 0,
    "password": 'abc',
    "expire_date": "2020-01-01",
    "balance": 0,
    "pay_day": 0,
    "id": None,
    "enroll_date": None,
    "credit": 15000
}