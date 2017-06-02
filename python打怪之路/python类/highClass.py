#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType


# 1. class 和 实例都能动态绑定属性和方法
def fun(self):
    print(self.name)


class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name

    # # 罗列出所有属性,实际是通过__dict__属性
    # def list_all_member(self):
    #     for name, value in vars(self).items():
    #         print("%s = %s" % (name, value))

# Student.score = 100
mark = Student('mark')
mark.age = 5
Student.fun = MethodType(fun, Student)
mark.fun()
# mark.score = 100  # 会报错
# AttributeError: 'Student' object has no attribute 'score'

# mark.list_all_member()
# print(mark.__dict__)


# 2. class 可以通过__slots__限制该类的实例能动态添加的属性,定义__slots__后__dict__就消失了
# Student.__slots__ = ('score',)
print(mark.__slots__)


# 3. __slots__对子类不起作用，子类如果定义__slots__的话，子类允许动态定义的属性是子类和父类的并集。
class subStudent(Student):
    pass
s = subStudent('jack')
s.score = 100  # 没有报错
print(subStudent.__slots__)


# @property设置getter, 生成@property.setter来设置setter，在setter中进行参数检查
class Person(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

a = Person()
a.birth = 2000
print(a.birth)
print(a.age)

# python 允许多继承 Mixin

