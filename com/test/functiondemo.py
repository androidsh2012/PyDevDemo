#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Created on 2016年1月12日

@author: suhan
@contact:  androidsh2012@gmail.com
@note: python基础练习——函数'''

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator




@log("excute")
def f(value):
    if not isinstance(value, (int, float)):
        raise TypeError('bad operand type')
    return abs(value)
print f(-100)
#print f('ABC')


#map/reduce
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
print map(f, [-1,2])
print map(lambda x: x*x, [y for y in range(10)])


class A(object):
    pass

a = A()        
print isinstance(a,A)     



class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth 
    
stu = Student()
stu._birth = 2000
print stu.age



try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
