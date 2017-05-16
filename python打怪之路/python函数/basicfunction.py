#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# python 函数输入输出
# 占位符 pass
def nop():
    pass

# 先说输出，输出好说
# python 函数没有返回值也会默认返回None
print(nop())


# 有多个返回值返回的是个tuple,自动对应到接受的对应变量里
def fun():
    return 1, 2, 3

print(fun())
m1, m2, m3 = fun()
print(m1, m2, m3)


# 有输入参数的最好进行输入参数检查
# python 输入参数的种类
# 位置参数（必选参数）,输入必须一一对应
# 默认参数 ，有默认值的参数，默认参数必须指向不变对象！
# 可变参数 *args
# 关键字参数  **kw
# 命名关键字参数

# 位置参数
def fun1(i1, i2):
    print(i1, i2)

fun1(1, 2)
fun1('1', '2')
fun1(i1='1', i2='2')
# fun1(1)  # TypeError: fun1() missing 1 required positional argument: 'i2'
# fun1(1, 2, 3)  # TypeError: fun1() takes 2 positional arguments but 3 were given
print('===========================')


# 默认参数
def fun2(i1=1, i2=2):
    print(i1, i2)

fun2(1, 2)
fun()
fun2(1)
fun2(i1=2)
fun2(i2=1)
fun2(i1=2, i2=1)


#


