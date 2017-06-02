#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time


def run(n):
    print("task", n, threading.current_thread())  # 输出当前的线程
    time.sleep(1)
    print('3s')
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')

starttime = time.time()

t_obj = []

for i in range(3):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.setDaemon(True)  # 把子进程设置为守护线程，必须在start()之前设置
    t.start()
    t_obj.append(t)

# print('active thread count: %d' % threading.active_count())  # 获取活跃线程数
# for t in t_obj:
#     t.join()
# print('active thread count: %d' % threading.active_count())

# print('cost: %s' % (time.time()-starttime))
# print(threading.current_thread())

time.sleep(1.5)  # 主线程停1.5秒后，主线程
print(threading.active_count())
# 主线程停1.5秒后，主线程结束，由于子线程全是主线程的守护线程，于是全部结束了。

