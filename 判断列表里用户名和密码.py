#!/usr/bin/env python
#_*_coding:utf-8_*_
# �жϵ�½�û��Ƿ����б��С�
# ����û����ڣ����ж������Ƿ�һ�£�
# ����û����ڣ����ж������Ƿ���ȷ
# ���������ȷ����ӡ�ͻ���Ϣ
users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},
 {'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},
 {'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]


name=raw_input('����������û�����')
for i in range(len(users)):
#    print users[i]['name']
    if name ==users[i]['name']:
        pwd=raw_input('���������룺')
        if pwd==users[i]['passwd']:
            print users[i]
            break
        else:
            print '�������'
            break
        
else:
    print '�û���������'


#����2
name_list=[]
passwd_lsit=[]

for i in users:
    name_list.append(i['name'])
    passwd_lsit.append(i['passwd'])
name=raw_input('�����û�����')
if name in name_list:
    pwd=raw_input('�������룺')
    if pwd==passwd_lsit[name_list.index(name)]:
        print users[name_list.index(name)]
    else:
        print 'passwd error'
else:
    print 'name error' 
    