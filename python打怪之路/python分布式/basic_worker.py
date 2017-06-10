#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def worker():
    # 通过名字注册queue
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接服务器
    server_addr = '127.0.0.1'
    print('Connect to server %s..' % server_addr)
    # 端口和验证码要一致
    manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    manager.connect()
    # 获取queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 从task获取任务，结果返回队列
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d..' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty')
    # 处理结果
    print('worker exit.')

if __name__ == '__main__':
    worker()

