#!/usr/bin/env python
#_*_coding:utf-8_*_
#дһ��֧����������list��������
#��ͬ�Ĵ���Ƭ�Σ�Ҫ��װ�ɺ��������ֲ�ͬ�ĵط����ò�������

my_list=[['192.168',10],['192.169',11],['192.166',12]]
my_list_dict=[{'ip':'192.111','count':32},{'ip':'192.12','count':10},{'ip':'192.131','count':22}]
def my_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j][1]>arr[j+1][1]:
                arr[j],my_list[j+1]=arr[j+1],my_list[j]
    return arr
print my_sort(my_list)
 
def my_sort1(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]['count']>arr[j+1]['count']:
                arr[j],my_list[j+1]=arr[j+1],my_list[j]
    return arr
print my_sort1(my_list_dict)