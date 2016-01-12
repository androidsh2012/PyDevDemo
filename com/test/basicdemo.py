# -*- coding: utf-8 -*-

'''
Created on 2016年1月12日

@author: androidsh2012
@contact:  androidsh2012@gmail.com
@note: python基础练习——字符串、判断、循环、字典
'''
#list列表
from __builtin__ import str
list = ['a','b','c']
print list[-1],len(list)
print list[1:3]

list.append('d')
list.insert(1, 'e')
print list

list.pop(2)
print list

list = ['123','456',['a','b'],True,u'呵呵']
print list[2][1],list[-1]

l = range(100)
print l[:10]
print l[:100:5]
print 'ABCDEFG'[:3],'ABCD'[::3]

str = u'windows微软'
print '%s' % str

# tuple元组，一旦初始化就不能修改
colors = ('black','white','green')
print colors

#判断和循环
score = 90
if score >= 90:
    print '优秀'
elif score < 60:
    print '不及格'
else:
    print '良好'
 
sum = 0
for i in range(0,10):
    sum = sum + i
print sum 

for color in colors:
    print color
    
dic = dict()
dic['c'] = 1
dic['b'] = 2
dic['a'] = 3
# d = {'苏轼':1,'苏洵':2,'苏辙':3}

for k,v in dic.iteritems():
    print k,v


print dic['a'],dic.get('b')
# 按照key进行排序
print sorted(dic.items(), key=lambda d: d[0])
# 按照value进行排序 
print sorted(dic.items(), key=lambda d: d[1],reverse=False)


s = set()
s.add(1)
s.add('abc')
s.add(2)
s.add(3)
s.add(1)
print s
s.remove(2)
print s

