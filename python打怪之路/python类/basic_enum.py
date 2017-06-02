#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 枚举类
from enum import Enum,unique
Month = Enum('Month', ['Jan', 'Feb', 'Mar', 'Apr', 'May'])

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 派生枚举类
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

# 成员的引用方式
print(Weekday.Mon)
print(Weekday['Mon'])
print(Weekday(1))
print(Weekday.Mon.value)
