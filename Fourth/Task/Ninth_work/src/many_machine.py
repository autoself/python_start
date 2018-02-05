#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-2-5 下午3:32'



import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import shared_information
from multiprocessing import Process,Pool



def __check_groupname(groupname):
    data = shared_information.group_machine()
    if not data:
        print('表示数据表不存在!')
        return False
    if groupname in data:
        return data
    else:
        print('没有找到相关的主机')
        return False

def __check_machine_list(groupname):
    data = shared_information.read_machine()
    if not data:
        print('表示数据表不存在!')
        return False
    for key in data:
        if data[key]['hostname'] == ipaddr:
            machine = data[key]
            break
    else:
        print('没有找到相关的主机')
        return False
    return machine

def one_command():
    machine_hostname = input('请输入需要远程执行的主机组>>>')
    command = input('请输入需要远程执行的命令>>>')
    group_data = __check_groupname(machine_hostname)
    if not group_data:
        return False





def one_download():
    machine_hostname = input('请输入需要远程执行的服务器主机组>>>')
    remote_file = input('远程的文件>>>')
    loacl_file = input('本地存放的文件>>')


def one_upload():
    machine_hostname = input('请输入需要远程执行的服务器主机组>>>')
    loacl_file = input('本地存放的文件>>>>')
    remote_file  = input('上传到服务器的文件>>>')




def run_many():
    info='''
    \033[35;1m------- One Machine View --------\033[0m
    \033[32;1m请选择:
    1.多机执行命令
    2.多机上传文件
    3.多机下载文件
    4.返回
    5.退出
    \033[0m
    '''
    nums = [1,2,3,4,5]
    check_status = False
    while not check_status:
        print(info)
        select_nums = input('Plase select nums>>>').strip()
        if select_nums.isdigit():
            select_nums = int(select_nums)
            if select_nums in nums:
                if select_nums == 1:
                    one_command()
                    continue
                elif select_nums == 3:
                    one_download()
                    continue
                elif select_nums == 4:
                    return True
                else:
                    return False

            else:
                print('选择有问题,请重新选择！')
                continue
        else:
            print('选择有问题,请重新选择！')
            continue