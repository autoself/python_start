#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-15 下午5:35'

import shutil,os
import logging


with open("/data/test/profile",'r',encoding='utf-8') as srcfile, open('/data/test/2.txt','w',encoding='utf-8') as drcfile:
    shutil.copyfileobj(srcfile,drcfile,length=10)


#shutil.copyfile("/data/test/README.md","/data/test/1.txt")

#shutil.copymode("/data/test/profile","/data/test/1.txt")

#shutil.copystat("/data/test/README.md","/data/test/1.txt")

#shutil.chown("/data/test/1.txt",'mango','mango')
#os.remove("/data/test/1.txt")
#shutil.copy2("/data/test/profile","/data/test/1.txt")
#os.remove("/data/test/1.txt")

#path_dir = os.path.dirname(os.path.abspath(__file__))
#shfile = os.path.join(path_dir,'shutil_01.log')
#logger = logging.getLogger()
#sh = logging.FileHandler(shfile)
#sfamter = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
#sh.setFormatter(sfamter)
#sh.setLevel(logging.DEBUG)

shutil.make_archive('/data/test/0.txt','gztar',root_dir='/data/test')

import zipfile,time

os.chdir('/data/test')

#zipnow = zipfile.ZipFile('/data/test/you.tar','w')
#zipnow.write('1.txt')
#zipnow.close()

zipnows = zipfile.ZipFile('/data/test/you.tar','r')
zipnows.extractall()
zipnows.close()

print(os.listdir())
print(os.path.dirname('/data/test/you.tar'))
print( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getatime('/data/test/you.tar'))) )



shutil.ignore_patterns()

