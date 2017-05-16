#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 变量与对象的区别
a = 'Abc'
# a 是变量，'Abc'是对象
b = a.replace('A', 'a')
print(b)
print(a)


# python中，字符串，整数，元组是不可变对象， 不可变对象本身的方法不会改变本身
# list 元素数据类型不限
l = [1, 2, 3]
# 通过索引获取元素
print(l[0])
print(l[-3])
# 追加元素到末尾
l.append(4)
print(l[3])
# pop()删除末尾元素,或pop(index)删除指定索引的元素
l.pop()
print(l)
l.pop(0)
print(l)
# 替换指定位置的元素直接赋值
l[0] = 1
print(l)
# list中含有list可以成为多维数组
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l1)
print(l1[2][0])


# tuple 元组不可变是指元素的指向不变，不是指指向的元素本身不变。tuple初始化后不可改变
t1 = (1, 2, 3)
p = [1, 2]
t2 = (1, p, 3)
print(t2)
p[1] = 3
print(t2)
# 单个元素tuple加逗号,python显示也会加逗号以区别括号
t3 = (1,)
print(t3)


# dict 要求key完全不可变
d = {'1': 1, '2': [2, 3]}
print(d)
d = {(1, 2, 3): 1, 2: 2}
print(d)
# d = {1: 1, (1, [2, 3]): 2}  # TypeError: unhashable type: 'list'
# 获取元素，通过key,通过get()方法,get()方法可以设置默认值
print("d[2]", d[2])
print("d[2]", d.get('2', -1))


# set 集合同数学概念集合,set中的元素必须是完全不可变的，与dict的key相同
# set 初始化set()，参数要求是一个可迭代的对象 ，比如list
s = {1, 2, 3}
print(s)

l = [1, 2, 3]
s1 = set(l)
print('s1:', s1)
# s1 = {1, [2, 3], 4}  # TypeError: unhashable type: 'list'
# print(s1)
s2 = {1, (2, 3), 4}
print(s2)
# s3 = {1, (2, [3, 4]), 5}  # TypeError: unhashable type: 'list'
# print(s3)
# 集合间可以做交并操作， &, |
ss1 = {1, 2}
ss2 = {2, 3}
ss = ss1 & ss2
print('ss:', ss)
ss = ss1 | ss2
print('ss:', ss)
# set 添加元素
s.add(3)
print('set add 3:', s)
s.add(4)
print(s)
# set 删除元素
s.remove(4)
print(s)


# dict 的key和 set一样都是不可重复，可以重复添加，但是只会保留最后一个
d1 = {
    '1': 1,
    '1': 2
}
print("d1:", d1)
s = {1, 2, 2, 3, 3}
print('s:', s)
