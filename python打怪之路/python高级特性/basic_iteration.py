#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 可迭代类型 Iterable
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function， 生成器可用next()迭代


# 迭代是从含有多个元素的对象中一个一个取出元素

# list tuple 迭代
for i in [1, 2, 3]:
    print(i)

for i in (1, 2, 3):
    print(i)


# dict迭代
for k in {'a': 1, 'b': 2}:
    print(k)

for v in {'1': 1, '2': 2}.values():
    print(v)

for k, v in {'4': 4, '5': 5}.items():
    print('k:', k, 'v:', v)


#  使用isinstance(object, Iterable) 来判断手否是可迭代对象。
from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))

# enumerate 把list变成索引元素对
for i, v in enumerate([1, 2, 3]):
    print(i, v)

# 同时引用两个变量
l = ((1, 2), (2, 4), (3, 6))
for x, y in l:
    print(x, y)


# 迭代器 Iterator
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数,

print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance({}, Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance('abc', Iterator))
print(isinstance(iter('abc'), Iterator))


