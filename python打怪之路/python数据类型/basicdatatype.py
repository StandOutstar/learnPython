#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "" 与 '' 的区别是，""中的'不用转义

# print('I'm ok')
print("I'm ok")

# print("I"m ok")
print("I\"m ok")

# 其他转义
# \n \t \\ %%
print('hello\nworld!')
print('hello\tworld!')
print('hello\\world!')
print('%d %%' % 70)

# r''表示字符串内部不转义
print(r'\n')

# ''''''表示多行内容,不用写换行符
print('''hello
my
friends''')

# None 与 ''
# type函数检测参数类型，dir函数检测参数的属性
none = None
null = ''
print(type(none))
print(type(null))
print(dir(none))
print(dir(null))


