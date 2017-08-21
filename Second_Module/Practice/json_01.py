#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-15 下午1:30'


import json
from io import StringIO

data = {'k2':123,'k1':345,'k4':789,'k3':567 }

j_str = json.dumps(data,sort_keys=True)
print(j_str)

with open('json.txt',encoding='utf-8',mode='w') as fd:
    json.dump(data,fd,sort_keys=True)



d = [ 'abcd','efgh']
io = StringIO()
js_str = json.dump(d,io)
print(io.getvalue())


import pickle

print(pickle.loads(pickle.dumps(data)))


import shelve
