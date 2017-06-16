#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 关于类
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def print_grade(self):
        print('name: %s  score: %d' % (self.__name, self.__score))


jack = Student('jack', 87)
jack.print_grade()

# 1. 类的访问限制是通过 在变量名前加双下划线来控制，加双下划线的不能直接通过变量名存取，(但实际是Python对变量名进行了变形，还是可以通过变形后的名字存取,可以通过dir()函数查看所有属性来查看变形后的名字) print(
# jack.__name) AttributeError: 'Student' object has no attribute '__name'
# print(dir(jack)) ['_Student__name',
# '_Student__score', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'get_name', 'get_score', 'print_grade', 'set_name', 'set_score']


# 2. 实例可以添加任意属性，不同实例可以有不同属性
mark = Student('mark', 60)
jones = Student('jones', 80)

mark.age = 20
print(mark.age)
# print(jones.age)
# AttributeError: 'Student' object has no attribute 'age'

# 3. 添加访问限制的属性，对她的直接赋值是无效的，相当于在实例中添加了一个新属性
jones.__score = 100
jones.print_grade()
# name: jones  score: 80, 可以发现没有改变属性的值
print(jones.__score)
# 反而是添加了一个新的属性，所以加了双下划线的属性实际存储的变量名发生了变化。


# 4. python 鸭子类型 即python中没有严格的类型约束，只要满足需要，是什么类型都可以， 即只"只要看起来像鸭子， 走起路来像鸭子就可以当作鸭子"， 这就是鸭子类型
def printSudentMark(student):
    student.print_grade()


class other(object):
    @staticmethod
    def print_grade():
        print('other')
oo = other()

printSudentMark(mark)
printSudentMark(oo)
# name: mark  score: 60
# other

# print(dir(mark))

# 5. 获取对象信息
# * type() 查看对象类型。
# * isinstance() 判断是否有继承关系。
# * dir() 查看所有属性和方法。


# 6. 实例属性和类属性， 实例属性优先级高于类属性
# 类属性不用加self，类属性归所有实例共用，所有实例都可访问
