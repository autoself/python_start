#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-8 下午2:33'




import queue

import time, threading

q = queue.Queue(maxsize=10)

def Product(name):
    count = 0
    while True:
        q.put('生产包子%s' % count)
        print('产包子%s' % count)
        count += 1
        time.sleep(0.2)


def Consumer(name):
    #while q.qsize() > 0:
    while True:
        print(' %s 吃包子 %s' % (name,q.get()))
        time.sleep(1)



p = threading.Thread(target=Product,args=('Alex',))
c = threading.Thread(target=Consumer,args=('Bill',))
d = threading.Thread(target=Consumer,args=('andylin',))

p.start()
c.start()
d.start()