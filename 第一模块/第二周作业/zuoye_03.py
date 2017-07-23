#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-7-23 下午4:36'


import sys,os

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


class CheckShop(object):
    def __init__(self,sm,opdir,dirjson,dirjsons):
        self.sm = sm
        self.opdir = opdir
        self.dirjson = dirjson
        self.dirjsons = dirjsons
        self.allshop = []
    def shopshow(self):
        with open(self.opdir,'r') as shf:
            sc = eval(shf.read())
        for k,v in enumerate(sc):
            print(k,v)
        return sc

    def selectshop(self,sc):
        inshop = input('Please shop nums:')
        if inshop.isdigit():
            inshop = int(inshop)
            if 0 <= inshop < len(sc):
                if inshop == (len(sc) -1):
                    with open(self.dirjson,'w') as f:
                        f.write(str(self.sm))
                    return True
                if sc[inshop][0] == 's':
                    ldj = open(self.dirjsons,'r')
                    print("History is showp list:")
                    for ljs in ldj:
                        print(ljs)
                    print("in the balance of \033[31m %s \033[0m" % self.sm)
                    print("#"*50)
                    return False

                mms = self.sm - sc[inshop][1]
                if mms < 0:
                    print("The goods purchased now  %s are in the balance of \033[31m %s \033[0m " % (self.allshop,self.sm))
                else:
                    self.sm = mms
                    self.allshop.append(sc[inshop][0])
                    with open(self.dirjsons,'a+') as djs:
                        djs.write(str(sc[inshop]))
                    print("The goods purchased now  %s are in the balance of \033[31m %s \033[0m " % (self.allshop,self.sm))
                return False
            else:
                print('The input is incorrect. Please re-enter it')
                return False
        else:
            print('The input is incorrect. Please re-enter it')
            return False

    def Mshop(self):
        sc = self.shopshow()
        ssp = self.selectshop(sc)
        if not ssp:
            self.Mshop()





def ShopInfo(username):
    path_dir = os.path.dirname(os.path.abspath(__file__))
    showdir = os.path.join(path_dir+os.sep+'shop')
    dirsj = os.path.join(path_dir + os.sep + 'shoplog')
    dir_join = os.path.join(dirsj+ os.sep + username)
    dirjions = os.path.join(dirsj+ os.sep + username+'_s')
    if not os.path.exists(dirsj):
        os.makedirs(dirsj)
    if os.path.exists(dir_join):
        with open(dir_join,'r') as f:
            nowsm = int(f.read())
            if nowsm > 0:
                print("in the balance of \033[31m %s \033[0m" % nowsm )
                cshops =  CheckShop(nowsm,showdir,dir_join,dirjions)
                cshops.Mshop()
                return True
    memory = input('Please moemory:')
    cshops = CheckShop(int(memory), showdir,dir_join,dirjions)
    cshops.Mshop()
    return True

def PwdInfo(username):
    password = input('password:').strip()
    cpcc = CheckPass(username,password)
    cpwd = cpcc.CheckPwd()
    if cpwd == 'Con':
        PwdInfo(username)
    elif cpwd == 'Succ':
        print('welcome to shop!!!')
        ShopInfo(username)
    else:
        print('The End!!')


if __name__ == "__main__":
    username = UserInput()
    if not username:
        sys.exit()
    password = PwdInfo(username)