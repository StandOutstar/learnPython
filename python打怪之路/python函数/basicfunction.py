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

# 位置参数 可传入参数名也可不传入
def fun1(i1, i2):
    print(i1, i2)

fun1(1, 2)
fun1('1', '2')
fun1(i1='1', i2='2')
# fun1(1)  # TypeError: fun1() missing 1 required positional argument: 'i2'
# fun1(1, 2, 3)  # TypeError: fun1() takes 2 positional arguments but 3 were given
print('===========================')


# 默认参数 默认参数必须指向不变对象！
def fun2(i1=1, i2=2):
    print(i1, i2)

fun2(1, 2)
fun()
fun2(1)
fun2(i1=2)
fun2(i2=1)
fun2(i1=2, i2=1)


# [] l在函数定义时不是指向不变对象，整数，字符串，tuple这些才是不变的对象
def foo(l=[]):
    l.append('end')
    return l

print(foo())
print(foo())
print(foo())


# 正确的定义方法
def foo1(l=None):
    if l is None:
        l = []
    l.append('end')
    return l

print(foo1())
print(foo1())
print(foo1())


# 可变参数 可以传入list
def fun3(i1, *args):
    print('i1:', i1)
    print('*args:', args)

fun3(1, *[2, 3, 4], *[5, 6])
# 可变参数的传入方式
# 1. 组装成list或tuple传入
li = [1, 2, 3]
fun3(0, *li)
fun3(0, *[1, 2, 3])
# 2. 直接传入
fun3(0, 1, 2, 3)


# 关键字参数 可以传入dict
def fun4(i1, *args, **kwargs):
    print('i1:', i1)
    print('*args:', args)
    print('**kwargs', kwargs)

# 关键字参数的输入方法：
# 1. 直接传入
fun4(0, *[1, 2, 3], *[0, 0], city='2', age='5')
# 2. 组装成dict传入
extra = {'city': '2', 'age': '5'}
fun4(0, *[1, 2, 3], *[0, 0], **extra)
fun4(0, *[1, 2, 3], *[0, 0], **{'city': '2', 'age': '5'})


# 命名关键字参数 明确指出有哪些参数是可接受的，必须传入参数名
def fun5(i1, *, city, age):
    print('i1:', i1)
    print('city:', city)
    print('age', age)

fun5(1, city='2', age='3')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, 'Beijing', 'Engineer', city=1, job=2)

