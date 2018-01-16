#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-9 上午11:01'



from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()