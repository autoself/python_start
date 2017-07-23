#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-7-23 下午9:19'


import os,sys



class CheckInfo(object):
    def __init__(self, osfile, chlist):
        self.osfile = osfile
        self.chlist = chlist

    def Infofile(self):
        for k in self.chlist:
            print("%s.%s" % (k,self.chlist[k]))
        seck = input('>>')
        if seck.isdigit() and 0 < int(seck) <= len(self.chlist):
            if int(seck) == 1:
                yuangong = input('请输入要查询的员工姓名(例如: Alex):')
                osf = open(self.osfile,'r')
                for line in osf:
                    if yuangong == line.split(" ")[0]:
                        print("%s的员工工资:%s" % (line.split(" ")[0],line.split(" ")[1]))
                        break
            elif int(seck) == 2:
                yuangong = input('请输入要修改员工和工资,用空格分隔(例如: Alex 10):')
                data = ""
                osf = open(self.osfile, 'r')
                for line in osf:
                    if yuangong.split(" ")[0] == line.split(" ")[0]:
                        line = yuangong + '\n'
                    data +=line
                with open(self.osfile,'w') as fs:
                    fs.writelines(data)
                print("修改成功!")
            elif int(seck) == 3:
                yuangong = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：")
                with open(self.osfile,'a+') as fs:
                    fs.write('\n%s' % (yuangong))
                print('增加成功！')
            elif int(seck) == 4:
                print('再见！')
                return True
        else:
            print('请输入合法!')
        self.Infofile()





if __name__ == "__main__":
    path_dir = os.path.dirname(os.path.abspath(__file__))
    osfile = os.path.join(path_dir + os.sep + 'info.txt')
    checklists = {1: '查询员工工资', 2: '修改员工工资', 3: '增加新员工记录', 4: '退出'}
    if not os.path.exists(osfile):
        print('This is info.txt not exist!')
        sys.exit()

    cinfo = CheckInfo(osfile,checklists)
    cinfo.Infofile()
