#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random, time, queue
from multiprocessing.managers import BaseManager


# 发送任务队列
task_queue = queue.Queue()
# 接受结果队列
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


def master():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000设置验证码
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动manager
    manager.start()
    # 获得通过网络访问获得的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 发送任务到队列里
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d..' % n)
        task.put(n)
    print('try get results..')
    for i in range(10):
        r = result.get(timeout=10)
        print('results: %s' % r)
    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    master()
