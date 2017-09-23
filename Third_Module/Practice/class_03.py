#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-20 上午10:07'


class Person(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age, school, score):
        super(Student,self).__init__(name,gender,age)
        self.name = name.upper()
        self.gender = gender.upper()
        self.school = school
        self.score = score