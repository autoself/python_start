#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-2-3 下午2:46'



import paramiko



def run():
    info='''
    \033[35;1m------- USER View --------\033[0m
    \033[32;1m请选择:
    1.查看所有的组
	2.查看某台服务器信息
	3.修改某台服务器信息
	4.添加新服务器信息
	5.添加新服务组
	6.删除服务器信息
	7.删除组服务器
	8.返回
    9.退出
    \033[0m
    '''
    print(info)
    nums = [1,2,3,4,5,6,7,8,9,10]
    check_status = False
    while not check_status:
        select_nums = input('Plase select nums>>>').strip()
        if select_nums.isdigit():
            select_nums = int(select_nums)
            if select_nums in nums:
                if select_nums == 1:
                    display_group()
                    continue
                elif select_nums == 2:
                    display_user_one()
                    continue
                elif select_nums == 3:
                    change_user_one()
                    continue
                elif select_nums == 4:
                    add_user()
                    continue
                elif select_nums == 5:
                    add_group()
                    continue
                elif select_nums == 6:
                    del_group()
                    continue
                elif select_nums == 7:
                    del_user()
                    continue
                elif select_nums == 8:
                    return True
                else:
                    return False

            else:
                print('选择有问题,请重新选择！')
                continue
        else:
            print('选择有问题,请重新选择！')
            continue