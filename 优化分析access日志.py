#!/usr/bin/env python
#_*_coding:utf-8_*_
my_dict={}
f=open('access_log.txt')
for line in f: #���Ա��������ļ���û��һ��
    #print line
    temp=line.split(' ')
    #print temp
    #ip=tmpe[0]
    #status=tmpe[8]
    tup=(temp[0],temp[8])  #����һ��Ԫ����Ϊ���ԣ���id��status��
    my_dict[tup]=my_dict.get(tup,0)+1 #���û��key��valueΪ0���о���ʾ��ǰֵ
print my_dict
f.close()

#���ֵ�ת��Ϊ�б�Ȼ�������ð������
my_list=my_dict.items()  #���ֵ�ת��Ϊ���б�
print my_list

#ð������
for j in range(len(my_list)):
    for i in range(len(my_list)-1-j):
        if my_list[i][1]>my_list[i+1][1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
print my_list

print my_list[:-6:-1]   #��Ƭ��

#���б������д��html
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