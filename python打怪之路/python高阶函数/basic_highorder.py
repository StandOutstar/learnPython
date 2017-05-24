#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map
# reduce
# filter
# sorted


# 函数名也是对象
print(abs(-10))
print(abs)
f = abs
x = abs(-10)
print(f)
print(x)
# f 指向abs后，就可以通过f调用abs了
print(f(-10))

# 可修改函数指向
# abs = 10
# print(abs(-19))
# TypeError: 'int' object is not callable

# 变量可以指向函数，函数可以接受变量，函数就可以接受函数
# 接受函数作为参数的函数就是高阶函数


def af(x, y):
    return x + y


def add(a, x, y):
    print(a(x, y))

add(af, 1, 2)


# map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(n):
    return n * n


l1 = map(f, [1, 2, 3, 4, 5])
print(list(l1))


# reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))


# filter()  接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 判断是否是奇数
def is_odd(x):
    return x % 2 == 1
# 滤除奇数
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))


# sorted(*args, key) 排序，可按照key指定的函数排序
print(list(sorted([2, -4, 5, -7, 8], key=abs)))