#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 闭包
# 返回函数的函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4, 5)
print(f())

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
# 调用函数f时，才真正计算求和的结果
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数

# 闭包需要注意的两点
# 1. 定义时的函数的局部变量会被新函数引用
# 2. 返回的函数不会立即执行，在调用时才执行


def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())
# 9
# 9
# 9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9


# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())
