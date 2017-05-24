#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 装饰器对应于面向对象里的装饰模式
# python既可以用函数实现，也可以用类实现
def log1(func):
    def wrapper(*args, **kwargs):
        print('begin call %s' % func.__name__)
        r = func(*args, **kwargs)
        print('end call %s' % func.__name__)
        return r
    return wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(text)
            print('begin call %s' % func.__name__)
            r = func(*args, **kwargs)
            print('end call %s' % func.__name__)
            return r
        return wrapper
    return decorator


@log1
def now1():
    print('2017-05-24')

now1()


@log2('excute')
def now2():
    print('2017-05-24')

now2()



