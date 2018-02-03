#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-2-3 下午3:56'



import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from src import infomaition_machine
from src import one_machine



def run():
    info='''
    \033[35;1m------- Machine select View --------\033[0m
    \033[32;1m请选择:
    1.机器信息
    2.单机器操作
    3.批量机器操作
    4.退出
    \033[0m
    '''
    nums = [1,2,3,4]
    check_status = False
    while not check_status:
        print(info)
        select_nums = input('Plase select nums>>>').strip()
        if select_nums.isdigit():
            select_nums = int(select_nums)
            if select_nums in nums:
                if select_nums == 1:
                  status = infomaition_machine.run()
                  if not status:
                      check_status = True
                  continue
                elif select_nums == 2:
                    status = one_machine.run()
                    if not status:
                        check_status = True
                    continue
                else:
                    check_status = True

            else:
                print('选择有问题,请重新选择！')
                continue
        else:
            print('选择有问题,请重新选择！')
            continue