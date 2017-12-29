#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-12-28 上午11:06'


import threading
import time
import os


def run(num):
    print('runing on number %s  ' % (num))

    time.sleep(3)
    print("------all status-------", threading.current_thread())


thread_list = []
start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run,args=('t--%s ' % i,))
    t.setDaemon(True)   #把当前线程设置为守护线程
    t.start()
    thread_list.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里
    #print('--all--',threading.current_thread())

#如果没有执行join 进行等待,则很快
#for j in thread_list:
#    j.join()


#threading.active_count()     显示线程的个数
#threading.current_thread()   显示线程的状态
print("------all master--------",threading.current_thread(),threading.active_count())
print("cost: ",time.time() - start_time)