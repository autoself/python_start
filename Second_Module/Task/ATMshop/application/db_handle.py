#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-24 下午9:27'

from os import path

def file_db_handle(dbengine):
    '''
    :param dbengine: connection db
    :return:
    '''
    db_path = path.join(dbengine['path'],dbengine['name'])
    return db_path


def db_handle(dbengine):
    '''
    commection if engine
    :param dbengine: the db connions set in settings
    :return:
    '''
    if dbengine['engine'] == 'file_storage':
        return file_db_handle(dbengine)