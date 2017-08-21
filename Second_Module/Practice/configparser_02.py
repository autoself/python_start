#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-11 下午1:05'


import configparser

config = configparser.ConfigParser()

config.read('config.ini')
print(config.sections())  # exclude: [DEFAULT]

print(config.defaults()['compression'])