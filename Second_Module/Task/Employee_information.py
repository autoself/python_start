#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-18 上午9:21'


import os
import sys
import re




def authDoCheckFile(infofile):
    def checkDefalut(func):
        def DoFile(*args,**kwargs):
            if not os.path.isfile(infofile):
                infodict = { 1:{'name':'Alex Li','age':22,'phone':13651054608,'dept':'IT','enroll_date':'2013-04-01'},\
                             2:{'name':'Jack Wang','age':30,'phone':13304320533,'dept':'HR','enroll_date':'2015-05-03'},\
                             3:{'name':'Rain Liu','age':25,'phone':13832353222,'dept':'Sales','enroll_date':'2015-04-22'},\
                             4:{'name':'Mack Cao','age':40,'phone':1356145343,'dept':'HR','enroll_date':'2009-03-01'}
                            }
                with open(infofile,'w',encoding='utf-8') as infile:
                    for key in infodict:
                        str_list = ','.join( [ str(i) for i in list(infodict[key].values()) ] )
                        if key == max(infodict.keys()):
                            infile.write("%s,%s" % (str(key),str_list))
                        else:
                            infile.write("%s,%s\n" % (str(key), str_list))
            return func(*args,**kwargs)
        return DoFile
    return checkDefalut


class Starff_Info_Class(object):
    def __init__(self,info_files):
        self.info_files = info_files
        self.feild = [ 'id','name','age' ,'phone','dept','enroll_date' ]


    def Check_value(self,checklist,field,value,checks):
        values_field = list(checklist.replace('\n','').split(','))
        if checks == 'like':
            if  value in values_field[int(field)]:
                return True
        elif checks == ">":
            if values_field[int(field)].isdigit():
                if  int(value) < int(values_field[int(field)]):
                    return True
        elif checks == '=':
            if  value == values_field[int(field)]:
                return True



    def Select_info(self,checklist,field=None,value=None,checks=None):
        num = 0
        with open(self.info_files,'r',encoding='utf-8') as infofiles:
            for line in infofiles:
                if len(checklist) == 6:
                    if field:
                        check_value = self.Check_value(line,field,value,checks)
                        if check_value:
                            print(line.replace('\n', ''))
                            num += 1
                    else:
                        print(line.replace('\n',''))
                        num += 1
                else:
                    nowlist = []
                    line_list = re.split(',',line.replace('\n',''))
                    for n in checklist:
                        nowlist.append(str(line_list[int(n)]))
                    str_lines = ','.join(nowlist)
                    if field:
                        check_value = self.Check_value(line,field,value,checks)
                        if check_value:
                            print(str_lines)
                            num += 1
                    else:
                        print(str_lines)
                        num +=1
        print("In Total Count:",num)


    def Check_field(self,field):
        checkfeild = []
        for i in range(len(self.feild)):
            if self.feild[i] in field:
                checkfeild.append(str(i))
        return checkfeild

    def Check_select(self,check_statinfo):
        str_info = re.split('\s+',check_statinfo)
        if str_info[0] == 'select' and str_info[2] == 'from' and str_info[3] == 'staff_table':
            if str_info[1] == '*':
                checkfeild = [ '0','1','2','3','4','5']
            else:
                sfield = re.split(',',str_info[1])
                checkfeild = self.Check_field(sfield)
            if len(str_info) == 4:
                self.Select_info(checkfeild)
            else:
                wh_info = re.split('\s+where\s+',check_statinfo)
                d_info = re.findall('\s*like\s*',wh_info[1])
                if d_info:
                    ds_info = re.split('\s+like\s+',wh_info[1])
                    d_feild = self.Check_field(ds_info[0].strip())[0]
                    d_value = re.findall('[a-zA-Z0-9]+',ds_info[1].strip())[0]
                    self.Select_info(checkfeild, d_feild, d_value, 'like')
                else:
                    dc_info = re.findall('[=|>|<]',wh_info[1])[0]
                    ds_info = re.split('\s+[=|>|<]\s+', wh_info[1])
                    d_feild = self.Check_field(ds_info[0].strip())[0]
                    d_value = re.findall('[a-zA-Z0-9]+', ds_info[1].strip())[0]
                    self.Select_info(checkfeild, d_feild, d_value, dc_info)
        else:
            print('Faild')
            return False


    def Check_delte(self,id):
        with open(self.info_files,'r',encoding='utf-8') as oldfile:
            oldlines = oldfile.readlines()

        with open(self.info_files,'w',encoding='utf-8') as newfile:
            for oldline in oldlines:
                oldid = list(oldline.split(','))[0]
                if str(oldid) != id :
                    newfile.write(oldline)

    def Check_Create(self,newline):
        newmax = 0
        newlist = list(newline.split(','))
        if len(newlist) == 5:
            if not str(newlist[1]).isdigit():
                return False
            if str(newlist[2]).isdigit() and len(newlist[2]) == 11:
                pass
            else:
                return False
        else:
            return False
        with open(self.info_files,'r+',encoding='utf-8') as oldfile:
            for line in oldfile:
                oldlist = list(line.split(','))
                oldid =int(oldlist[0])
                if  oldid > newmax:
                    newmax = oldid
                if str(newlist[2]) == oldlist[3]:
                    return False
            newmax +=1
            oldfile.write('%s,%s' % (str(newmax),newline) )
            return True

    def Check_Update(self,upline):
        checkup = re.match('(update|UPDATE)\s+(staff_table)\s+(SET|set)\s+(.*)\s+(WHERE|where)\s+(.*)',upline)
        if checkup:
            check_set = re.sub('(update|UPDATE)\s+(staff_table)\s+(SET|set)\s+','',upline)
            check_list = re.split('\s+(WHERE|where)\s+',check_set)
            change_list = re.split('\s*(=)\s*',check_list[0])
            change_field = self.Check_field(change_list[0])
            change_value = re.sub('[\"|\']','',change_list[2])
            set_list = re.split('\s*(=)\s*',check_list[2])
            set_field = self.Check_field(set_list[0])
            set_value = re.sub('[\"|\']','',set_list[2])
            with open(self.info_files,'r',encoding='utf-8') as oldfile:
                oldlines = oldfile.readlines()
            with open(self.info_files,'w',encoding='utf-8') as newfile:
                for oldline in oldlines:
                    line_list = list(oldline.replace('\n','').split(','))
                    if line_list[int(set_field[0])] == set_value:
                        line_list[int(change_field[0])] = change_value
                    str_list = ','.join(line_list)
                    newfile.write(str_list+'\n')
            return True
        else:
            return False




path_dir = os.path.dirname(os.path.abspath(__file__))
fo_files = os.path.join(path_dir,'staff_table')

@authDoCheckFile(infofile= fo_files)
def First_func(fo_files):
    check_judgment = True
    while check_judgment:
        print("#"*60)
        print(
              "1.查询        2. 创建新员工\n"
              "3.删除员工    4.可修改员工\n"
              "5.退出"
              )
        print("#"*60)
        checknum = input("Please nums>>>").strip()
        if checknum.isdigit():
            intnum = int(checknum)
            if 0 <  intnum <= 5:
                if intnum == 5:
                    print("Thank you for your use! Bye!")
                    check_judgment = False
                elif intnum == 1:
                    check_sinfo = input("Please ( select * from staff_table ) >>>").strip()
                    ch = Starff_Info_Class(fo_files)
                    ch.Check_select(check_sinfo)
                elif intnum == 2:
                    check_newinfo = input("Please ('name','age' ,'phone','dept','enroll_date') >>>")
                    ch = Starff_Info_Class(fo_files)
                    checknew = ch.Check_Create(check_newinfo)
                    if checknew:
                        print('Create new Success!')
                    else:
                        print('Create new \033[31m Faild! \033[0m')
                elif intnum == 3:
                    check_delinfo = input("Please (id) >>>").strip()
                    ch = Starff_Info_Class(fo_files)
                    ch.Check_delte(check_delinfo)
                elif intnum == 4:
                    check_upinfo = input('Please ( UPDATE staff_table SET dept="Market" WHERE dept = "IT" ) >>>').strip()
                    ch = Starff_Info_Class(fo_files)
                    chup = ch.Check_Update(check_upinfo)
                    if chup:
                        print('Update now Success!')
                    else:
                        print('Update now \033[31m Faild! \033[0m')
            else:
                print("Sorry, your input is incorrect!")
        else:
            print("Sorry, your input is incorrect!")

    return True



First_func(fo_files)


