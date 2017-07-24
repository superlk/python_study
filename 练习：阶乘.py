#!/usr/bin/env python
#_*_coding:utf-8_*_
#阶乘就是6！=6*5*4*3*2*1

def jiecheng(num):
    res=1
    for i in range(1,num+1):
        res *=i
    return res
num=int(raw_input('请输入阶乘数字：'))
jiecheng(num)

#递归用法

#6!=6*5!  
#1!=1
def fib(num):
    if num==1:
        return 1
    return num*fib(num-1)
num=int(raw_input('请输入阶乘数字：'))
print fib(num)
