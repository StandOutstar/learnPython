#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

secret_code = 'qwerxxixxwerewrxxlovexxsdfwerxxyouxxwerds'

# .的用法
a = 'xy123'
b = re.findall('x..', a)  # 匹配x后跟两个任意字符
print(b)
# ['xy1']

# *的用法
a = 'xxy1xx23x'
b = re.findall('xx*', a)  # 匹配x, xx
print(b)
# ['xx', 'xx', 'x']

# ?的用法
a = 'xxy1xx23x'
b = re.findall('xy?', a)  # 匹配x, xy
print(b)
# ['x', 'xy', 'x', 'x', 'x']

# .*贪心算法
b = re.findall('xx.*xx', secret_code)
print(b)
# ['xxixxwerewrxxlovexxsdfwerxxyouxx']

# .*?非贪心算法
b = re.findall('xx.*?xx', secret_code)
print(b)
# ['xxixx', 'xxlovexx', 'xxyouxx']

# ()用法
b = re.findall('xx(.*?)xx', secret_code)
print(b)
# ['i', 'love', 'you']

secret_code = '''qwerxxi
xxwerewrxxlovexxsdfwerxxyouxxwerds'''

b = re.findall('xx(.*?)xx', secret_code)
print(b)
# ['werewr', 'sdfwer']

# re.S的用法
b = re.findall('xx(.*?)xx', secret_code, re.S)
print(b)
# ['i\n', 'love', 'you']

# search的用法
s2 = 'qwerxxixxwexxlovexxwexxyouxx'
s = re.search('xx(.*?)xxwexx(.*?)xx', s2).group(1)
print(s)
# i
s = re.search('xx(.*?)xxwexx(.*?)xxwexx(.*?)xx', s2).group(2)
print(s)
# love
s = re.search('xx(.*?)xxwexx(.*?)xxwexx(.*?)xx', s2).group(3)
print(s)
# you

# sub 的用法
s3 = '123sssss123'
s = re.sub('123(.*?)123', '123%s123' % 'world', s3)
print(s)
# 123world123

# 按整型替换
s = re.sub('123(.*?)123', '123%d123' % 666, s3)
print(s)

# 按字符型替换
s = re.sub('123(.*?)123', '123%123' % 666, s3)
print(s)