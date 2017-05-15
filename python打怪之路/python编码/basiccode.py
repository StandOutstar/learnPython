#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

# python3 字符串默认是以unicode编码，支持中文
print('你好世界！')

# ord()函数获取字符的整数表示
print(ord('你'))
print(ord('好'))

# chr()函数把编码转换为对应的字符
print(chr(20320))

# 字符整数编码转换为16进制写str
print('\u4f60\u597d')

# bytes类型
s = 'abc'
b = b'abc'
print(s)
print(b)

# 以unicode表示的 str 通过encode()方法可以编码为指定的bytes(ascii 一个byte, utf-8中文3个byte)
# 网络传输或磁盘读写要转换为bytes， str 通过 encode 变为 bytes , bytes再通过 decode 变为 str
# 为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
h = 'hello world!'
h1 = h.encode('ascii')
print(h1)
print(h1.decode('ascii'))

# len() 函数可以计算字符串的字符数 或 bytes的字节数
print(len(h))
print(len(h1))


# 格式化 ， %s %f %d %x
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 如果不知道该用哪个就用%s
print('age: %s, point: %s, male: %s' % (17, 8.5, True))
# 格式化含有%时，用%%转义
print('%d %%' % 70)

s1 = 72
s2 = 85
r = (85 - 72)/72*100
print('%.1f%%' % r)
