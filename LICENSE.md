#!/usr/bin/env python
#_*_coding:utf-8_*_
arr=[1,3,7,10,22,100,299,1000]
num_to_find=input('please input your num:')
start=0
end=len(arr)-1
count=0
while True:
    count +=1
    mid=(start+end)/2
    mid_num=arr[mid]
    #print start,end,mid,mid_num
    if mid==start:
        print "can not find ,shoul after %s==>%s"%(start,arr[start])
        break
    if num_to_find<mid_num:
        end=mid
    elif num_to_find>mid_num:
        start=mid
    else:
        print 'find',mid
        break
print count
