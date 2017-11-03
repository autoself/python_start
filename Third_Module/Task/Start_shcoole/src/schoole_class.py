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

    def __init__(self,teacher_db,course_db,class_db,name,course_name,teacher,semester='第一期'):
        '''
        :param teacher_db:     讲师db表
        :param course_db:      课程db表
        :param class_db:       班级db表
        :param name:           班级名
        :param course_name:    课程名
        :param teacher:        讲师名
        :param semester:       学期
        '''

        self.name =  name
        self.course_name = course_name
        self.semester = semester
        self.teacher = teacher
        self.__teacher_db = teacher_db
        self.__course_db = course_db
        self.__class_db = class_db

    def __check_db(self,db,name):
        '''
        查询
        :return:
        '''
        if os.path.isfile(db):
            with open(db,'rb') as fs:
                data = pickle.load(fs)
            if data:
                for key in data:
                    if data[key]['name'] == name:
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
        check_course = self.__check_db(self.__course_db,self.course_name)
        if check_course:
            print('课程不存在,请先创建课程!')
            return False
        check_teacher = self.__check_db(self.__teacher_db,self.teacher)
        if check_teacher:
            print('讲师不存在,请先创建讲师！')
            return False
        check_class = self.__check_db(self.__class_db,self.name)
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
        db[maxid] = {'name': self.name, 'semester': self.semester, 'course_name': self.course_name,'teacher':self.teacher}
        with open(self.__class_db, 'wb') as fp:
            pickle.dump(db, fp)
        return True
