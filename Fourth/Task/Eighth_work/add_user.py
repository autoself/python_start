#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午9:59'


from etc import setting

import json
import hmac
import os
import sys
import shutil
#from collections import defaultdict
#http://www.cnblogs.com/wupeiqi/articles/4911365.html


def adduser(username,password,disksize):
    '''
     添加用户
    :param username: 用户名
    :param password: 密码
    :param disksize: 目录大小限制(B)
    :return:
    '''
    if os.path.isfile(setting.DB_FILE):
        with open(setting.DB_FILE,'r',encoding='utf8') as fs:
            data = json.load(fs)

        for key in data:
            if data[key]['username'] == username:
                print('%s 用户名 %s 已存在了,请重新输入！ %s' % (setting.RED,username,setting.RESET) )
                return True
        else:
            if not data:
                nums = 1
            else:
                nums = int(max(data))
                nums += 1
            pwd = hmac.new(password.encode('utf8'),setting.DB_PWD_MD5.encode('utf8'))         #加密

    else:
        if not os.path.isdir(setting.DB_DIR):
            os.makedirs(setting.DB_DIR)
        nums = 1
        data = {}
        pwd = hmac.new(password.encode('utf8'),setting.DB_PWD_MD5.encode('utf8'))
        #二级字典
        # newdata = {}
        # newdata['username'] =username
        # newdata['password'] = pwd.hexdigest()
        # data[nums] = newdata
    data.update({nums: {'username': username, 'password': pwd.hexdigest(), 'disksize': disksize}})  # 添加新的内容二级字典
    try:
        with open(setting.DB_FILE,'w',encoding='utf-8') as fp:
            json.dump(data,fp)
    except:
        print('%s  用户名 %s 添加失败！请联系管理人员！ %s' % (setting.RED,username,setting.RESET))
    else:
        userdir = os.path.join(setting.USER_DIR,username)
        if not os.path.isdir(userdir):
            os.makedirs(userdir)
        print('%s 用户名 %s 添加成功 %s' % (setting.GREEN,username,setting.RESET))



def changepwd(username,password):
    '''
    修改用户密码
    :param username: 用户名
    :param password: 密码
    :return:
    '''
    if os.path.isfile(setting.DB_FILE):
        with open(setting.DB_FILE,'r',encoding='utf8') as fs:
            data = json.load(fs)

        for key in data:
            if data[key]['username'] == username:
                pwd = hmac.new(password.encode('utf8'), setting.DB_PWD_MD5.encode('utf8'))
                data[key].update({'username': username, 'password': pwd.hexdigest(),'disksize':data[key]['disksize']})
                with open(setting.DB_FILE, 'w', encoding='utf8') as fb:
                    json.dump(data,fb)
                print('%s 此用户%s 密码修改成功 %s' % (setting.GREEN, username, setting.RESET))
                return True
    print('%s 此用户%s是不存在的！%s' % (setting.RED,username,setting.RESET))



def changedisk(username,disksize):
    '''
    磁盘大小修改
    :param username: 用户名
    :param disksize: 磁盘大小
    :return:
    '''
    if os.path.isfile(setting.DB_FILE):
        with open(setting.DB_FILE,'r',encoding='utf8') as fs:
            data = json.load(fs)

        for key in data:
            if data[key]['username'] == username:
                data[key].update({'username': username, 'password': data[key]['password'],'disksize':disksize})
                with open(setting.DB_FILE, 'w', encoding='utf8') as fb:
                    json.dump(data,fb)
                print('%s 此用户%s 目录大小限制修改成功,大小:%s %s' % (setting.GREEN, username,disksize, setting.RESET))
                return True
    print('%s 此用户%s是不存在的！%s' % (setting.RED,username,setting.RESET))



def deletename(username):
    '''
    注销用户
    :param username: 用户名
    :return:
    '''
    if os.path.isfile(setting.DB_FILE):
        with open(setting.DB_FILE,'r',encoding='utf8') as fs:
            data = json.load(fs)

        for key in data:
            if data[key]['username'] == username:
                data.pop(key)
                try:
                    with open(setting.DB_FILE,'w',encoding='utf8') as fb:
                        json.dump(data,fb)
                except:
                    print('%s 用户%s 注销失败 %s' % (setting.GREEN, username, setting.RESET))
                    return False
                else:
                    userdir = os.path.join(setting.USER_DIR, username)
                    if os.path.isdir(userdir):
                        shutil.rmtree(userdir)
                    print('%s 用户%s 注销成功 %s' % (setting.GREEN, username, setting.RESET))
                    return True
    print('%s 此用户%s是不存在的！%s' % (setting.RED, username, setting.RESET))


def listuser():
    if os.path.isfile(setting.DB_FILE):
        with open(setting.DB_FILE,'r',encoding='utf8') as fs:
            data = json.load(fs)
        for key in data:
            print('%s有用户名为: %s  所受目录大小为:%s  %s' % (setting.RED,data[key]['username'],data[key]['disksize'] ,setting.RESET))

def auoput():
    sys.exit()

def run():
    info = '''
    \033[35;1m------- USER View --------\033[0m
    \033[32;1m请选择:
    1、查看所有用户
	2、添加新用户
	3、修改用户密码
	4、用户目录大小修改
	5、注销用户
	6、退出
    \033[0m
    '''
    print(info)
    datalist = [1,2,3,4,5,6]
    checkstatus = False
    while not checkstatus:
        nums = input('>>>')
        if nums.isdigit():
            nums = int(nums)
            if nums in datalist:
                if nums == 2:
                    username  = input('请输入用户名>>>')
                    password =  input('请输入密码>>>')
                    disksize = input('请输入目录大小限制(B)>>')
                    adduser(username,password,disksize)
                elif nums == 3:
                    username = input('请输入用户名>>>')
                    password = input('请输入密码>>>')
                    changepwd(username, password)
                elif nums == 1:
                    listuser()
                elif nums == 4:
                    username = input('请输入用户名>>>')
                    disksize = input('请输入目录大小限制(B)>>')
                    changedisk(username,disksize)
                elif nums == 5:
                    username = input('请输入用户名>>>')
                    deletename(username)
                elif nums == 6:
                    checkstatus = True
                    print('%s 感谢你的使用! %s' %(setting.GREEN,setting.RESET))
            else:
                print('%s 你输入有误,请重新再来! %s' % (setting.RED, setting.RESET))
        else:
            print('%s 你输入有误,请重新再来! %s' % (setting.RED,setting.RESET))

if __name__ == '__main__':
    run()