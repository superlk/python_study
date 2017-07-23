#!/usr/bin/env python
#_*_coding:utf-8_*_
a = [1,23,34,23,23,67,434,34]
'''
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print a
print a[-1]
'''
max=0
for i in a:
    if i >max:
        max=i
print max