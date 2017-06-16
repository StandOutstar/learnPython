#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# open没有文创建文件，没有文件打开文件。
f = open('tset.txt', 'w')
# 写入文件
f.write('2017年6月1日 15:58:18')
f.close()
f = open('tset.txt', 'r')
print(f.read())
f.close()

f = open('tset.txt', 'a+')
f.write('2017年6月1日 16:02:06')
f.close()
f = open('tset.txt', 'r')
print(f.read())
f.close()

# 使用上下文读写
with open('tset.txt', 'a') as f:
    f.write('2017年6月1日 16:11:50')

with open('tset.txt', 'r') as f:
    print(f.read())

# 内存读写 StringIO和BytesIO的接口与文件读写一致
