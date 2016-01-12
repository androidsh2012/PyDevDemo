#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Created on 2016年1月12日

@author: androidsh2012
@contact:  androidsh2012@gmail.com
@note: python基础练习——线程2'''

import threading,time
   
class SubThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
         
    # override run
    def run(self):
        time.sleep(0.1)
        print '[%s] ' % self.name
        counter(10)
       
def counter(n):
    count = 0
    for i in xrange(n):
        i += 1
        count += i
    print '%d' % count
   
   
def main():
    for i in xrange(3):
        i += 1
        thd = SubThread('thread-' + str(i))
        thd.start()
        thd.join()      # 阻塞主线程，等待子线程先结束   
       
# 测试
if __name__ == '__main__':  
    main()
    print('-_-')
    
