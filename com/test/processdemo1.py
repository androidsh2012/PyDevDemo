#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Created on 2016年1月12日

@author: androidsh2012
@contact:  androidsh2012@gmail.com
@note: python基础练习——线程1'''

import threading,time
#用于线程执行的函数
def counter(n):
    sum = 0;
    for i in xrange(n):
        sum += i;
        print i
        time.sleep(1)
    print sum;            
                        
if __name__ == '__main__':
    
    th = threading.Thread(target=counter, args=(3,));
    th.start();
    th.join(); #主线程阻塞等待子线程结束
    print '-_-'
    
