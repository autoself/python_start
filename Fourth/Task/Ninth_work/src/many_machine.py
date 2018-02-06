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
        print('表示主机组数据表不存在!')
        return False
    if groupname in data:
        return data
    else:
        print('没有找到相关的主机组')
        return False

def __check_machine_list(groupname):
    data = shared_information.read_machine()
    if not data:
        print('表示数据表不存在!')
        return False
    machine_list = {}
    for key in data:
        if data[key]['groups'] == groupname:
            machine_list.update({key:data[key]})
    if machine_list:
        return machine_list
    else:
        return False


def one_command():
    machine_hostname = input('请输入需要远程执行的主机组>>>')
    command = input('请输入需要远程执行的命令>>>')
    group_data = __check_groupname(machine_hostname)
    if not group_data:
        return False
    machine_data = __check_machine_list(machine_hostname)
    if not machine_data:
        return machine_data

    process_pool = Pool(4)
    for key in machine_data:
        process_pool.apply_async(func=shared_information.ssh_command,args=(machine_data[key]['ipaddr'],machine_data[key]['username'],machine_data[key]['password'],machine_data[key]['port'],command))

    process_pool.close()
    process_pool.join()


def one_download():
    machine_hostname = input('请输入需要远程执行的服务器主机组>>>')
    remote_file = input('远程的文件>>>')
    loacl_file = input('本地存放的文件>>')
    group_data = __check_groupname(machine_hostname)
    if not group_data:
        return False
    machine_data = __check_machine_list(machine_hostname)
    if not machine_data:
        return machine_data

    process_pool = Pool(4)
    for key in machine_data:
        process_pool.apply_async(func=shared_information.ssh_command, args=(machine_data[key]['ipaddr'], machine_data[key]['username'], machine_data[key]['password'],machine_data[key]['port'], remote_file,loacl_file))

    process_pool.close()
    process_pool.join()

def one_upload():
    machine_hostname = input('请输入需要远程执行的服务器主机组>>>')
    loacl_file = input('本地存放的文件>>>>')
    remote_file  = input('上传到服务器的文件>>>')
    group_data = __check_groupname(machine_hostname)
    if not group_data:
        return False
    machine_data = __check_machine_list(machine_hostname)
    if not machine_data:
        return machine_data

    process_pool = Pool(4)
    for key in machine_data:
        process_pool.apply_async(func=shared_information.ssh_command, args=(machine_data[key]['ipaddr'], machine_data[key]['username'], machine_data[key]['password'],machine_data[key]['port'], remote_file, loacl_file))

    process_pool.close()
    process_pool.join()


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