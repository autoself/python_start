#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-12-23 下午3:23'


import threading
import time


class MyThread(threading.Thread):

    def __init__(self,num):
        #threading.Thread.__init__(self)
        super(MyThread,self).__init__()
        self.num = num



    def run(self):
        print('runing on number %s ' % self.num)

        time.sleep(3)



if __name__ == '__main__':

    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()


