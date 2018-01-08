#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-4 下午2:12'


import threading
import time


def daka():
    count = 0
    while True:
        if count > 0 and count < 5:
            if event.isSet():
                event.set()
            print('\033[42;1m--green open on---\033[0m')
        elif count >= 5 and count < 10:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red close on---\033[0m')
        else:
            count = 0
            event.set()
        time.sleep(1)
        count +=1

def mens():
    while 1:
        time.sleep(1)
        if event.isSet():
            print('men go to door ...')
        else:
            print('men close door .....')


if __name__ == '__main__':

    event = threading.Event()
    dk = threading.Thread(target=daka)
    dk.start()
    for i in range(3):
        t = threading.Thread(target=mens)
        t.start()
