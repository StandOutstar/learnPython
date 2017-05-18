#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list tuple str 有切片语法


# list 切片 还是list
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l1[0:3])
print(l1[7:])
print(l1[-3:])
print(l1[:])
print(type(l1[:]))

# tuple 切片 还是tuple
t1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t1[0:3])
print(t1[7:])
print(t1[-3:])
print(t1[:])
print(type(t1[:]))

# str 切片 还是str
str1 = '0123456789'
print(str1[0:3])
print(str1[7:])
print(str1[-3:])
print(str1[:])
print(type(str1[:]))
