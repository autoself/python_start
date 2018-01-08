#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-4 上午11:07'

import threading, time


def run(n):
    global  num
    semaphore.acquire()
    time.sleep(1)
    num += 1
    print("run the thread: %s\n" % num)
    semaphore.release()


if __name__ == '__main__':

    num = 0
    semaphore = threading.BoundedSemaphore(3)  # 最多允许5个线程同时运行
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    print(num)
