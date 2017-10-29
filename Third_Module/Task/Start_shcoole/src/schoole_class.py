#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-16 下午9:32'


import os
import pickle
import time

class School_Class(object):
    '''
    班级
    '''

    def __init__(self,course_db,class_db,name,course_name,semester='第一期'):
        '''
        :param name:        班级名
        :param semester:    学期
        :param course_name: 课程
        '''

        self.name =  name
        self.semester = semester
        self.course_name = course_name
        self.__course_db = course_db
        self.__class_db = class_db


    def __select_course(self):
        '''
        获取课程
        :return:
        '''
        if os.path.isfile(self.__course_db):
            with open(self.__course_db,'rb') as fs:
                course_db = pickle.load(fs)
            if course_db:
                for key in course_db:
                    if course_db[key]['name'] == self.course_name:
                        return True
        return False

    def __check_class(self):
        '''
        获取班级
        :return:
        '''
        if os.path.isfile(self.__class_db):
            with open(self.__class_db,'rb') as fs:
                class_db = pickle.load(fs)
            if class_db:
                for key in class_db:
                    if class_db[key]['name'] == self.name:
                        return False
        return True


    def __max_course_id(self):
        '''
        获取最大的id
        :return:
        '''
        if os.path.isfile(self.__class_db):
            with open(self.__class_db,'rb') as fs:
                db = pickle.load(fs)
            if db:
                maxnums = max(db)
                return maxnums
        return 0

    def create_class(self):
        check_course = self.__select_course()
        if not check_course:
            print('课程不存在,请先创建课程!')
            return False
        check_class = self.__check_class()
        if not check_class:
            print('班级已经存在,无须再创建！')
            return False
        maxnums = int(self.__max_course_id())
        if maxnums != 0:
            with open(self.__class_db, 'rb') as fs:
                db = pickle.load(fs)
                print(db)
        else:
            db = {}
        maxid = maxnums + 1
        create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        db[maxid] = {'name': self.name, 'semester': self.semester, 'course_name': self.course_name,'starttime':create_time}
        with open(self.__class_db, 'wb') as fp:
            pickle.dump(db, fp)
        return True
