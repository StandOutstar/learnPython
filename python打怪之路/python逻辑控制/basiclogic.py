#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for name in ['1', '2', '3']:
    print(name)

names = ['1', '2', '3']

for i in range(3):
    print(names[i])

n = 0
while n < 3:
    print(names[n])
    n += 1


# 利用dict实现类似switch
'''
def fun1():
    print("using 1")


def fun2():
    print("using 2")


def fun3():
    print("using 3")

switch = {
    '1': fun1,
    '2': fun2,
    '3': fun3
}
x = input()
switch[x]()
'''
# 利用lambda和dict实现switch
'''
result = {
    'a': lambda y: y * 5,
    'b': lambda y: y + 7,
    'c': lambda y: y - 2
}
print(result['b'](3))
'''

# 自定义switch类
