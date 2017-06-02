#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 类定制，通过各种定制方法实现类的定制，以生成特定的类
# __str__  定制打印类信息
# __iter__  定制类可迭代
# __getitem__  定制类可用下标取
# __getattr__  定制类属性获取
# 利用__getattr__可实现链式调用，以方便的编写API
# __call__  定制类本身可调用


class Chain(object):

    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain().users('Michael').repo)
