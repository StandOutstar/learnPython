#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lambda 匿名函数
# Python支持有限


# 匿名函数用以代替函数, 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
def f():
    return lambda x: x * x
fs = f()
print(fs(3))




# 1.先来看第一个lambda:x+y

def fn1():
    x, y = 1, 2
    return lambda:x+y


# >>> fn()()
# 3
# limbda里面没有参数，所以x， y是fn1里面定义的x，y


# 2.再来看第二个lambda x，y：x+y
def fn2():
    x, y = 1, 2
    return lambda x, y:x+y


# >>> fn2()()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: <lambda>() missing 2 required positional arguments: 'x' and 'y'
# 由报错知，说是lambda缺少两个参数，所以

# >>> fn2()(3,4)
# 7


# 3.第三个lambda x=x，y=y：x+y

def fn3():
    x, y = 1, 2
    # 或者lambda m = x，n = y:m+n
    return lambda x = x, y = y: x+y


# >>> fn3()()
# 3
# lambda里面定义了m和n，再将x，y分别赋值给m和n,相当于设置了默认值
print(fn3()(4, 5))
