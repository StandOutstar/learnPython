#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

# 偏函数
# functools.partial把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，使调用这个新函数会更简单

logging.info(int('1000', base=2))
logging.info(int('123', base=10))


import functools

int2 = functools.partial(int, base=2)
logging.info(int2('1000'))
logging.info(int2('1000', base=10))

max2 = functools.partial(max, 10)
logging.info(max2(5, 6, 7))

