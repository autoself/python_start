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

    def __init__(self,teacher_db,class_db,numbers,name,grade,school_class):
        '''
        :param numbers        讲师编号
        :param name:          讲师名
        :param grade          讲师级别
        :param school_class   所在的班级
        '''

        self.numbers  = numbers
        self.grade = grade
        self.name = name
        self.school_class = school_class
        self.__teacher_db = teacher_db
        self.__class_db = class_db


    def __check_class(self):
        '''
        获取班级
        :return:
        '''
        if os.path.isfile(self.__class_db):
            with open(self.__class_db, 'rb') as fs:
                class_db = pickle.load(fs)
            if class_db:
                class_list = []
                for key in class_db:
                    class_list.append(class_db[key]['name'])
                now_list = set(self.school_class).difference(set(class_list))
                if now_list:
                    return False
        return True


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
                    if thearch_db[key]['numbers'] == self.numbers:
                        return True
        return False



    def create_teacher(self):
        check_class = self.__check_class()
        if  check_class:
            print('班级不存在,请先创建班级！')
            return False
        maxnums = int(self.__select_maxid())
        if maxnums != 0:
            with open(self.__teacher_db, 'rb') as fs:
                db = pickle.load(fs)
                print(db)
        else:
            db = {}
        maxid = maxnums + 1
        db[maxid] = {'numbers': self.numbers, 'name': self.name, 'grade': self.grade, 'schoole_class':self.school_class }
        with open(self.__teacher_db, 'wb') as fp:
            pickle.dump(db,fp)
        return True


