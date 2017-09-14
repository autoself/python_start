#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-30 下午2:15'

import logging
def logger(log_type):
    '''
    :param log_type: access or transaction or others
    :return: obj or logger
    '''
    #create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)


    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create file handler and set level to warning
    log_file = 'log_test.log'
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


#a = logger('Test')

#a.info("sda")
#a.info("hu")
#a.info("ji")

#logger("log test...").info("sda")
#logger("log test...").info("hu")
#logger("log test...").info("ji")

