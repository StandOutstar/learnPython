#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# python异常处理
try:
    pass
except Exception as e:
    print(e)
finally:
    pass


# raise 抛出异常
raise Exception('error')

# 在except捕获异常时也可继续抛出
try:
    pass
except Exception as e:
    pass
    raise

# 还可转换异常
try:
    pass
except Exception as e:
    pass
    raise ValueError('input error')
