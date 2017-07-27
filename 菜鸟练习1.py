#!/usr/bin/env python
#_*_coding:utf-8_*_
#date：2017。7.27
#mail:651002081@qq.com
#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
for i in range(1,5):
    for j in range(1,5):
        for n in range(1,5):
            if i!=j and j!=n and i!=n:
                print i,j,n
                
