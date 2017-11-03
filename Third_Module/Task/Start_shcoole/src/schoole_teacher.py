#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-16 下午9:36'


import os
import pickle

class Teacher(object):

    '''
       讲师
    '''

    def __init__(self,teacher_db,name,schoole_city):
        '''

        :param teacher_db:      讲师数据表
        :param name:            讲师名
        :param schoole_name:    学校名
        '''

        self.name = name
        self.schoole_city = schoole_city
        self.__teacher_db = teacher_db



    def __select_maxid(self):
        '''
        获取最大的ID
        :return:
        '''
        if os.path.isfile(self.__teacher_db):
            with open(self.__teacher_db,'rb') as fs:
                thearch_db = pickle.load(fs)
            if thearch_db:
                for key in thearch_db:
                    if thearch_db[key]['name'] == self.name:
                        return True
        return False



    def create_teacher(self):
        maxnums = int(self.__select_maxid())
        if maxnums != 0:
            with open(self.__teacher_db, 'rb') as fs:
                db = pickle.load(fs)
                print(db)
        else:
            db = {}
        maxid = maxnums + 1
        db[maxid] = {'name': self.name,'schoole_city':self.schoole_city }
        with open(self.__teacher_db, 'wb') as fp:
            pickle.dump(db,fp)
        return True


