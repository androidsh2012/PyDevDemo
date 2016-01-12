#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Created on 2016年1月12日

@author: androidsh2012
@contact:  androidsh2012@gmail.com
@note: python基础练习——正则表达式'''

import re

m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)

str = "Hi, Python: 010-1234567"
match = re.search(r'(\w+), (\w+): (\S+)', str)
print match.group(1),match.group(2),match.group(3)

str = 'This is a \n normal string'
rawstr = r'and this is a\n raw string'
print str
print rawstr


s='123 \n456 \n789'
print re.findall(r'.+',s)   # 点符号匹配的是除了换行符'\n'以外的所有字符
print re.findall(r'.+' , s , re.S)


line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"


#compile同类上
rec = re.compile(r'dogs')   
print rec.search(line).group()


