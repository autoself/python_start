#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-25 上午9:16'


'''
可以对指定机器异步的执行多个命令
例子：
>>:run "df -h" --hosts 192.168.3.55 10.4.3.4 
task id: 45334
>>: check_task 45334 
>>:
注意，每执行一条命令，即立刻生成一个任务ID,不需等待结果返回，通过命令check_task TASK_ID来得到任务结果 
'''

import pika
import uuid
import sys
import re
import time
import random
import threading
import json

class RpcClient(object):
    '''
      rpc客户端的调用
    '''
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='127.0.0.1'))  #实例化

        self.channel = self.connection.channel() #管道

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.call_requese, no_ack=True,
                                   queue=self.callback_queue)

    def call_requese(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


    def send_server(self, uuid,msg):
        self.response = None
        self.corr_id = uuid
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_cmd',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       content_type='application/json',
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(msg))

        while self.response is None:
            self.connection.process_data_events()
            time.sleep(0.5)
        return self.response




def remote_sender(cmd):
    '''
    调用rcp发送远端服务器
    :param cmd: 输入时的命令
    :return:
    '''
    uuid = str(int(time.time())) + uuid_num()
    ipaddr = re.findall(r'\d+\.\d+\.\d+\.\d+', cmd)
    if '\'' in cmd:
        commond = cmd.split('\'')[1]
    elif '\"' in cmd:
        commond = cmd.split('\'')[1]
    msg = {
        'cmd': commond,
        'host': ipaddr
    }
    cmd_rpc = RpcClient()

    run_process = threading.Thread(target=cmd_rpc.send_server, args=(uuid, json.dumps(msg)))
    run_process.setDaemon(True)  #守护线程的形式,无需等待结果
    run_process.start()

    task_queue = {uuid:cmd_rpc}
    return task_queue




def uuid_num():
    num = []
    while(len(num)<5):
        x=random.randint(0,9)
        if str(x) not in num:
            num.append(str(x))
    data = ''.join(num)
    return data

def run():
    check_status = False
    info = u'''
        \033[35;1m------- Help Please cmd ---------\033[0m
        \033[34;1m
        1. run 'command' --hosts ip ip ... 返回uuid
        2. check_task uuid  返回结果
        3. tasklist 查看现有的taskid
        4. exit        
        \033[0m
    '''
    task_queue = {}
    while not check_status:
        print(info)
        cmd = input('>>>').strip()
        if not cmd: continue
        if re.match(r'run\s+[\'|\"](.*)[\'|\"]\s+\-\-hosts\s+(\d{1,3}\.){3}\d{1,3}.*\s*$',cmd):
            data = remote_sender(cmd)
            for key in data.keys():
                task_queue[key] = data[key]
                print('task id:', key)
        elif re.match(r'check_task\s+\d*\s*$',cmd):
            cmd = cmd.split()
            if cmd[1] in task_queue.keys():
                msg = task_queue[cmd[1]].response
                if msg:
                    print(msg.decode('utf8'))
                else:
                    print('\033[1;32;1m正在获取结果，稍后再试.....\033[0m')
        elif re.match(r'tasklist',cmd):
            if task_queue:
                for key in task_queue.keys():
                    print('\033[1;32;1mtask id: %s \033[0m' % key)
        elif cmd == 'exit':
            sys.exit()
        else:
            print('\033[1;37;41m输入有误,请按正确格式输入! !\033[0m')





if __name__ == '__main__':
    run()
