#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = "D:\\表情包\\产品\\产品经理专属表情包-起点学院学习联盟\\产品经理斗图专用表情包100张"
# path = "D:\\表情包\\程序员"
print(os.listdir(path))
i = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        index = file.index('.')
        new_name = file.replace(file, "p%d" % i + file[index:])
        # print(index)
        os.rename(os.path.join(path,file), os.path.join(path, new_name))
        i += 1
print('END')


