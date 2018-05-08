#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-25 上午9:15'



import pika
import time
import subprocess
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_cmd')



def commond(cmd):
    try:
        cmd_status = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        cmd_result = cmd_status.stdout.read()
        cmd_status.stdout.close()
        cmd_error = cmd_status.stderr.read()
        cmd_status.stderr.close()
    except Exception as e:
        raise  e
    finally:
        if cmd_result:
            return cmd_result
        else:
            return cmd_error


def host_list(hostlist,name,cmd):
    str_list = ''
    for host in hostlist:
        info = '''
        Host: {0}
        commond:{1}
        {2}
        '''.format(host,name,cmd.decode('utf8'))
        str_list += info
    return str_list

def on_request(ch, method, props, body):
    response = body
    json_dict = json.loads(response)
    cmd = commond(json_dict['cmd'])
    clinet_cmd = host_list(json_dict['host'],json_dict['cmd'],cmd)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                          correlation_id= props.correlation_id
                          ),
                     body=str(clinet_cmd))
    ch.basic_ack(delivery_tag=method.delivery_tag)


#channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_cmd')

print(" [x] Awaiting RPC requests")
channel.start_consuming()






