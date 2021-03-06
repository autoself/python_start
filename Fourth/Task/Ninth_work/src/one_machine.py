#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-2-3 下午2:55'


import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import shared_information


def __check_hostname(ipaddr):
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
    machine_hostname = input('请输入需要远程执行的服务器主机名>>>')
    command = input('请输入需要远程执行的命令>>>')
    machine = __check_hostname(machine_hostname)
    if not machine:
        return False
    shared_information.ssh_command(machine['ipaddr'],machine['username'],machine['password'],machine['port'],command)




def one_download():
    machine_hostname = input('请输入需要远程执行的服务器主机名>>>')
    remote_file = input('远程的文件>>>')
    loacl_file = input('本地存放的文件>>')
    machine = __check_hostname(machine_hostname)
    if not machine:
        return False
    shared_information.ssh_download(machine['ipaddr'], machine['username'], machine['password'], machine['port'],remote_file,loacl_file)


def one_upload():
    machine_hostname = input('请输入需要远程执行的服务器主机名>>>')
    loacl_file = input('本地存放的文件>>>>')
    remote_file  = input('上传到服务器的文件>>>')
    machine = __check_hostname(machine_hostname)
    if not machine:
        return False
    shared_information.ssh_upload(machine['ipaddr'], machine['username'], machine['password'], machine['port'],remote_file, loacl_file)


def run_one():
    info='''
    \033[35;1m------- One Machine View --------\033[0m
    \033[32;1m请选择:
    1.单机执行命令
    2.单机上传文件
    3.单机下载文件
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


