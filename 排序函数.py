#!/usr/bin/env python
#_*_coding:utf-8_*_
def my_sort(args): 
    for j in range(len(args)):
        for i in range(len(args)-1-j):
            if args[i]>args[i+1]:
                args[i],args[i+1]=args[i+1],args[i]
    return args

print my_sort([3,2,4,1])
    
    
    