#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-31 下午1:56'


import logging
def logger(log_type,log_file_name):
    '''
    :param log_type: access or transaction or others
    :return: obj or logger
    '''
    #create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.DEBUG)


    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler and set level to warning
    log_file = log_file_name
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.WARNING)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


afile='test_02.log'
logger('test',afile).info('a')
logger('test',afile).info('b')
logger('test',afile).info('c')