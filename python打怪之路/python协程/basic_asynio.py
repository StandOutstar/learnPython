#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from greenlet import greenlet


def fun1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def fun2():
    print(56)
    gr1.switch()
    print(78)

if __name__ == '__main__':
    gr1 = greenlet(fun1)
    gr2 = greenlet(fun2)
    gr1.switch()
