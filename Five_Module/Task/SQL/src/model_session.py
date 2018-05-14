#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-5-14 下午10:10'

import os
import sys

BASEHOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEHOME)

from etc import setting
from sqlalchemy.orm import sessionmaker

def session_db():
    Session_class = sessionmaker(bind=setting.engine)
    Session = Session_class()
    return Session
