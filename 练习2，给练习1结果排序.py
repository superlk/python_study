#!/usr/bin/env python
#_*_coding:utf-8_*_
dic={'a': 8, 'e': 5, 'd': 6, 'g': 3, 'f': 5, 'i': 7, 'h': 6, 'k': 1, 'm': 2, 'l': 1, 'o': 1, 'n': 1, 's': 10, 'u': 1, 'w': 1, 'y': 1}
lis=[]
for k in dic:
    lis.append([k,dic[k]])
print lis
#Ã°ÅİÅÅĞò
for i in range(len(lis)):
    for j in range(len(lis)-1):
        if lis[j][1]>lis[j+1][1]:
            lis[j],lis[j+1]=lis[j+1],lis[j]
print lis
for r in lis[-10:]:
    print r