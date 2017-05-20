#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
# logging.basicConfig(level=logging.INFO)

# 生成器存储的是数据的计算规则，存储的是算法

# 生成器的两种定义方法:
# 1. 由列表生成式改为生成器
'''
G = (x * x for x in range(10))
print(G)
# <generator object <genexpr> at 0x000001E9D5A350F8>
print(next(G))
print(next(G))
print(next(G))
# 在调用最后一个next()会产生StopIteration的错误


# 2. 函数中写yield, 每次遇到yield返回，下次从yield后继续计算
def gen():
    for x in range(10):
        yield x

g = gen()
print(g)

# 使用迭代的方式打印每个元素，不是产生StopIteration的错误
for l in g:
    print(l)
'''


# 杨辉三角练习
def triangles():
    n = 0
    lastl = [1, 1]
    while n < 1000:
        if n == 0:
            yield [1]
        elif n == 1:
            yield [1, 1]
        else:
            # logging.info('lastl: %s' % lastl)
            origin = [1, 1]
            for i in range(len(lastl)-1):
                logging.info('lastl: %s' % lastl)
                logging.info('i : %s' % i)
                logging.info('lastl[%s]: %s' % (i, lastl[i]))
                logging.info('lastl[%s]: %s' % (i + 1, lastl[i + 1]))
                origin.insert(-1, lastl[i]+lastl[i+1])
                logging.info('origin: %s' % origin)
            lastl = origin
            yield lastl
        n = n + 1


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


