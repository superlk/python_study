#!/usr/bin/env python
#_*_coding:utf-8_*_
#�׳˾���6��=6*5*4*3*2*1
'''
def jiecheng(num):
    res=1
    for i in range(1,num+1):
        res *=i
    return res
num=int(raw_input('������׳����֣�'))
jiecheng(num)
'''
#6!=6*5!  
#1!=1
def fib(num):
    if num==1:
        return 1
    return num*fib(num-1)
num=int(raw_input('������׳����֣�'))
print fib(num)