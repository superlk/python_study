#!/usr/bin/env python
#_*_coding:utf-8_*_

arr=[]
list=[]
f=open('access_log.txt')
for i in f.read().split('\n'):
   temp=i.split()
   arr.append(temp[0])
   list.append(temp[8])
print arr
print list

f.close()

my_ip={}
my_status={}
for key  in range(len(list)):
    if list[key] == '200':
        if arr[key] in my_ip:
            my_ip[arr[key]]+=1
        else:
            my_ip[arr[key]]=1
    else:
        if arr[key] in my_status:
            my_status[arr[key]]+=1
        else:
            my_status[arr[key]]=1
print my_ip
print my_status

print '-'*10,'200ÅÅÐò','-'*10
arr_list=my_ip.items()
print arr_list
for j in  range(len(arr_list)-1):
    for k in range(len(arr_list)-1):
        #print arr_list[k]
        if arr_list[k][1]>arr_list[k+1][1]:
            arr_list[k],arr_list[k+1]=arr_list[k+1],arr_list[k]
print arr_list
acc_list=my_status.items()
print '-'*10,'404ÅÅÐò','-'*10
for m in  range(len(acc_list)-1):
    for n in range(len(acc_list)-1):
        #print arr_list[k]
        if acc_list[n][1]>acc_list[n+1][1]:
            acc_list[n],acc_list[n+1]=acc_list[n+1],acc_list[n]
print acc_list[-1][0]
f=open('id.html','w+')
s_tem='<tr><td>%s</td><td>%s</td><td>%s</td></tr>'
html_str='<table border="1">'
html_str+=s_tem%('IP','status','count')
for z,x in arr_list[:-5:-1]:
    html_str+=s_tem%(z,200,x)
for z,x in acc_list[:-5:-1]:
    html_str+=s_tem%(z,404,x)
html_str+='</table>'
f.write(html_str)
f.close()