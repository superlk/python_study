#!/usr/bin/env python
#_*_coding:utf-8_*_
my_dict={}
f=open('access_log.txt')
for line in f: #可以遍历整个文件，没次一行
    #print line
    temp=line.split(' ')
    #print temp
    #ip=tmpe[0]
    #status=tmpe[8]
    tup=(temp[0],temp[8])  #定义一个元组作为可以，（id，status）
    my_dict[tup]=my_dict.get(tup,0)+1 #如果没有key，value为0，有就显示当前值
print my_dict
f.close()

#把字典转换为列表，然后遍历，冒泡排序
my_list=my_dict.items()  #把字典转换为吏列表
print my_list

#冒泡排序
for j in range(len(my_list)):
    for i in range(len(my_list)-1-j):
        if my_list[i][1]>my_list[i+1][1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
print my_list

print my_list[:-6:-1]   #切片。

#把列表遍历，写入html
for (ip,status),count in my_list[:-6:-1]:
    print ip,status,count
f=open('access.html','w')
html_temp='<tr><td>%s</td><td>%s</td><td>%s</td></tr>'
html='<table border="1">'
html+=html_temp%('IP','s    tatus','count')
for (ip,status),count in my_list[:-6:-1]:
    html+=html_temp%(ip,status,count)
html+='</table>'
f.write(html)
f.close()