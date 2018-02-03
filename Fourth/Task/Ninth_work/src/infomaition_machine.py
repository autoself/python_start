#!/usr/bin/env python
#-*- coding:utf-8 -*-
from _sitebuiltins import _Printer

__author__ = 'andylin'
__date__ = '18-1-26 下午4:38'




import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from etc import setting

from src import  logger


accesslog = logger.logger('access')
errorlog = logger.logger('error')



def __user_r_table():
    try:
        with open(setting.DB_USER, 'r', encoding='utf-8') as fr:
            data = json.load(fr)
    except IOError:
        errorlog.error('Database User table reading is a problem')
        return False
    finally:
        return data

def __user_w_table(data):
    try:
        with open(setting.DB_USER, 'w', encoding='utf-8') as fw:
            json.dump(data,fw)
    except IOError:
        errorlog.error('Database User table wrtite is a problem')
        return False
    finally:
        return True

def add_user():
    '''
    添加新服务器
    :return:
    '''
    hostname = input('请输入主机名>>>').strip()
    ipaddr = input('请输入ip地址>>>').strip()
    username = input('请输入用户名>>>').strip()
    password = input('请输入密码>>>').strip()
    port = input('请输入ssh端口>>>').strip()
    groups = input('请输入所属服务器组>>>').strip()


    if not os.path.isfile(setting.DB_GROUP):
        errorlog.error('请选输入先输入服务器组')
        return False
    else:
        data_group = __group_r_table()
        if not data_group:
            return False
        if groups not in data_group:
            errorlog.error('请选输入先输入服务器组')
            return False

    if os.path.isdir(setting.DB_DIR):
        if os.path.isfile(setting.DB_USER):
            try:
                with open(setting.DB_USER, 'r', encoding='utf-8') as fr:
                    data = json.load(fr)
            except IOError:
                errorlog.error('Database User table reading is a problem')
                return False
            finally:
                if not data:
                    data = {}
        else:
            data = {}
    else:
        os.makedirs(setting.DB_DIR)
        data = {}

    if not data:
        nums = 1
    else:
        nums = len(data)
        nums += 1
    data.update({nums:{'hostname':hostname,'ipaddr':ipaddr,'username':username,'password':password,'port':port,'groups':groups}})
    status = __user_w_table(data)
    if status:
        print('添加新服务器信息成功!!!!')
        return True
    else:
        print('添加新服务器信息失败!!!!')
        return False


def display_user_one():
    '''
    展查某台服务器信息
    :return:
    '''
    if os.path.isfile(setting.DB_USER):
        data = __user_r_table()
        if not data:
            print('不好意思暂时还没有数据可查')
            return False
        else:
            ipaddr = input('请输入要查询的ip地址>>>').strip()
            for key in data:
                if data[key]['ipaddr'] == ipaddr:
                    print('服务器信息: %s' % data[key])
                    break
            else:
                print('没有查到相关的服务器信息')
                return False
    else:
        print('不好意思暂时还没有数据可查')
        return False


def change_user_one():
    '''
    修改服务器相关信息
    :return:
    '''
    if os.path.isfile(setting.DB_USER):
        data = __user_r_table()
        if not data:
            print('不好意思暂时还没有数据')
            return False
        else:
            ipaddr = input('请输入要修改的ip地址>>>').strip()
            for key in data:
                if data[key]['ipaddr'] == ipaddr:
                    hostname = input('请输入主机名>>>').strip()
                    ipaddr = input('请输入ip地址>>>').strip()
                    username = input('请输入用户名>>>').strip()
                    password = input('请输入密码>>>').strip()
                    port = input('请输入ssh端口>>>').strip()
                    groups = input('请输入所属服务器组>>>').strip()
                    data.update({key: {'hostname': hostname, 'ipaddr': ipaddr, 'username': username,'password': password, 'port': port, 'groups': groups}})
                    status = __user_w_table(data)
                    if status:
                        print('修改成功！')
                        return True
                    else:
                        print('修改失败！')
                        return False
            else:
                print('没有相关的服务器信息')
                return False
    else:
        print('不好意思暂时还没有数据')
        return False



def display_group():
    '''
    展示所有的服务器组
    :return:
    '''
    if os.path.isfile(setting.DB_GROUP):
        data = __group_r_table()
        if not data:
            return False
        else:
            print('\033[32;1m所有服务器组有:\033[0m \033[35;1m %s \033[0m' % data)
            return True
    else:
        print('不好意思暂时还没有数据')
        return False

def __group_r_table():
    '''
    读取服务器组的表
    :return:
    '''
    try:
        with open(setting.DB_GROUP, 'r', encoding='utf-8') as fr:
            data = json.load(fr)
    except IOError:
        errorlog.error('Database Group table reading is a problem')
        return False
    finally:
        return data


def __group_w_table(data):
    '''
    写入服务器组的表
    :param data:
    :return:
    '''
    try:
        with open(setting.DB_GROUP,'w',encoding='utf8') as fw:
            json.dump(data,fw)
    except:
        errorlog.error('写入用户组表失败!请检查系统!')
        return False
    finally:
        return True


def add_group():
    '''
    新添加服务器组
    :return:
    '''
    if os.path.isdir(setting.DB_DIR):
        if os.path.isfile(setting.DB_GROUP):
            data = __group_r_table()
            if not data:
                return False
        else:
            data = []
    else:
        os.makedirs(setting.DB_DIR)
        data = []

    group_name = input('请输入服务器组>>>').strip()

    if group_name in data:
        errorlog.error('输入的服务器组已经存在!')
        return False
    data.append(group_name)
    status = __group_w_table(data)
    if status:
        print('添加新服务器组成功!!!!')
        return True
    else:
        print('添加新服务器组失败!!!!')
        return False



def del_group():

    if os.path.isfile(setting.DB_GROUP):
        data_group = __group_r_table()
        if not data_group:
            return False
        else:
            group_name = input('请输入要删除用户组名>>>').strip()
            if group_name in data_group:
                data_user = __user_r_table()
                if data_user:
                    for key in data_user:
                        if data_user[key]['groups'] == group_name:
                            data_user.pop(key)
                    print(data_user)
                    return
                    status_user = __user_w_table(data_user)
                    if status_user:
                        data_group.remove(group_name)
                        status_group = __group_w_table(data_group)
                        if status_group:
                            print('删除服务器组成功！')
                            return True
                print('删除服务器组失败！')
                return False

            else:
                print('没有找到你要删除的服务器组')
                return False
    else:
        print('不好意思暂时还没有数据')
        return False

def del_user():
    if os.path.isfile(setting.DB_USER):
        data = __user_r_table()
        if not data:
            print('不好意思暂时还没有数据')
            return False
        else:
            ipaddr = input('请输入需要删除的ip信息>>>').strip()
            for key in data:
                if data[key]['ipaddr'] == ipaddr:
                    data.pop(key)
                    status = __user_w_table(data)
                    if status:
                        print('删除成功')
                    else:
                        print('删除失败!')
                    break
            else:
                print('没有查到相关的服务器信息')
                return False
    else:
        print('不好意思暂时还没有数据')
        return False




def run():
    info='''
    \033[35;1m------- Machine Info View --------\033[0m
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
    nums = [1,2,3,4,5,6,7,8,9]
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


