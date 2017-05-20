#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 迭代是从含有多个元素的对象中一个一个取出元素

# list tuple 迭代
for i in [1, 2, 3]:
    print(i)

for i in (1, 2, 3):
    print(i)


# dict迭代
for k in {'1': 1, '2': 2}:
    print(k)

for v in {'1': 1, '2': 2}.values():
    print(v)

for k, v in {'4': 4, '5': 5}.items():
    print('k:', k, 'v:', v)


#  使用isinstance(object, Iterable) 来判断手否是可迭代对象。
from collections import Iterable

print(isinstance([], Iterable))

# enumerate 把list变成索引元素对
for i, v in enumerate([1, 2, 3]):
    print(i, v)

# 同时引用两个变量
l = ((1, 2), (2, 4), (3, 6))
for x, y in l:
    print(x, y)

