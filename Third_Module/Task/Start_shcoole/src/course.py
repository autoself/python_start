#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-16 下午9:18'



import os
import pickle
import json


class Course(object):
    '''
      课程的创建
    '''

    def __init__(self,course_db,name,price,outline):
        '''
        :param name:  课程名
        :param price: 课程价格
        :param outline: 课程周期
        :param __db_file:  课程的数据表 相当于数据库表
        '''
        self.name = name
        self.price = price
        self.outline = outline
        self.__db_file = course_db

    def __max_course_id(self):
        '''
        获取最大的id
        :return:
        '''
        if os.path.isfile(self.__db_file):
            with open(self.__db_file,'rb') as fs:
                db = pickle.load(fs)
            if db:
                maxnums = max(db)
                return maxnums
        return 0

    def __check_name(self):
        '''
        课程唯一性
        :return:
        '''
        if os.path.isfile(self.__db_file):
            with open(self.__db_file,'rb') as fs:
                db = pickle.load(fs)
            for key in db:
                if db[key]['name'] == self.name:
                    return True
        return False

    def create_course(self):
        '''
        创建课程
        :return:
        '''
        check_name = self.__check_name()
        if check_name:
            print('课程已经存在了,无法再创建了!')
            return False
        maxnums = int(self.__max_course_id())
        if maxnums !=0 :
            with open(self.__db_file,'rb') as fs:
                db = pickle.load(fs)
        else:
            db = {}
        maxid = maxnums + 1
        db[maxid] = {'name': self.name, 'price': self.price, 'outline': self.outline}
        with open(self.__db_file, 'wb') as fp:
            pickle.dump( db,fp)
        return True


#if __name__  == '__main__':
#    a = Course('BeiJing','openlinux','16000','3m')
#    c= a.create_course()


