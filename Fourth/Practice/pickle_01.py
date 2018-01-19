#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 下午2:23'



import json


data = { 'k1':'adfa','k2':'ddd' }

with open('file.pk','w') as fp:
    json.dump(data,fp)