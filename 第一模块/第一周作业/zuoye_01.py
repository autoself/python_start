#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-7-23 上午10:26'

import sys,os,time

class CheckUsr(object):
    def __init__(self,usrname,opfile='user.txt'):
        self.username = usrname
        self.opfile = opfile

    def Usercheck(self):
        f = open(self.opfile,'r')
        for line in f:
            user = line.split(" ")[0]
            if self.username == user:
                return True
        return False

def UserInput():
    UserNmae = input('Username:').strip()
    User = CheckUsr(UserNmae)
    cUser = User.Usercheck()
    if not cUser:
        checkct = input('User is not exist!Do you need to continue?[y|n]')
        if checkct in ['y','yes','Yes','YES']:
            UserInput()
        else:
            return False
    return UserNmae


class CheckPass(object):
    def __init__(self,username,password,opfile='user.txt'):
        self.username = username
        self.password = password
        self.opfile = opfile

    def Pwdnum(self,stfile):
        if os.path.exists(stfile):
            with open(stfile, 'r+') as sf:
                line = sf.read()
                if len(line) == 3:
                    print('%s is lock!!!' % self.username)
                    return False
                else:
                    sf.write('1')
                    return True
        else:
            with open(stfile,'a+') as sf:
                sf.write('1')
            return True

    def CheckPwd(self):
        path_dir = os.path.dirname(os.path.abspath("__file__"))
        stdir = os.path.join(path_dir + os.sep + 'status')
        if not os.path.exists(stdir):
            os.makedirs(stdir)
        stfile =  os.path.join(stdir + os.sep + self.username)
        f = open(self.opfile,'r')
        for line in f:
            user = line.split(" ")[0]
            pwd = line.split(" ")[1].strip()
            if user == self.username:
                checkLock = self.Pwdnum(stfile)
                if checkLock:
                    if pwd == self.password:
                        if os.path.isfile(stfile):
                            os.remove(stfile)
                        print('Login Success!!!')
                        return 'Succ'
                    return 'Con'
                else:
                    return False


def PwdInfo(username):
    password = input('password:').strip()
    cpcc = CheckPass(username,password)
    cpwd = cpcc.CheckPwd()
    if cpwd == 'Con':
        PwdInfo(username)
    elif cpwd == 'Succ':
        print('welcome to python!!!')
    else:
        print('The End!!')


if __name__ == "__main__":
    username = UserInput()
    if not username:
        sys.exit()
    password = PwdInfo(username)
