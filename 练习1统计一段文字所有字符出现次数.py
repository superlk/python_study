#!/usr/bin/env python
#_*_coding:utf-8_*_

tup='my asasdf name i liu kai wo shi shei shei sehi hhe aadf sdfas dfasdf gsdgg'
#key :´ÎÊý
dic={}
count=0
for i in tup:
    if i==' ':
        continue
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print dic
print str(dic)



