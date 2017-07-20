#!/usr/bin/env python
#_*_coding:utf-8_*_
res={'a': 8, 'e': 5, 'd': 6, 'g': 3, 'f': 5, 'i': 7, 'h': 6, 'k': 1, 'm': 2, 'l': 1, 'o': 1, 'n': 1, 's': 10, 'u': 1, 'w': 1, 'y': 1}
#先把dic反转
res_reverse={}
for k in res:
    if res[k] in res_reverse:
        res_reverse[res[k]].append(k) #如果有value相同的在把k加入到新的字典的value里
    else:
        res_reverse[res[k]]=[k]
#  
key_list=[]  
for r in res_reverse:    
    key_list.append(r)
    key_list.sort()
count=0
while count<10:
    val=key_list.pop()  #把列表里最后一个值（最大值）复制给val，
    for k in res_reverse[val]:
        print 'char %s,count is %s'%(k,val)
        count+=1