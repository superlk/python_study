#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
#ȷ���ļ����Ƿ����û��������û�д�����
while True:
    username=raw_input('�����˻�')
    f=open('user.txt')
    user_dict={}
    arr=f.read().split('\n')
    for  line in  arr:
        if line:   #�����Ϊ��
            temp=line.split(':')
            user_dict[temp[0]]=temp[1]
            print user_dict
    f.close()
    
    if username in user_dict:
        print 'user exists'
    else:
        password=raw_input('��������')
        f=open('user.txt','a')
        f.write('\n'+username+':'+password)
        f.close()
        break
'''
#�޸�������ôд
# �����û���������У��޸����룬���û�У�����
print'-'*10,'�޸�����','-'*10
user_dict_new={}
username_new=raw_input('��������û�����')
f=open('user.txt')
for  line in  f.read().split('\n'):
    if line:   #�����Ϊ��
        temp_new=line.split(':')
        user_dict_new[temp_new[0]]=temp_new[1]
print user_dict_new
f.close()
if username_new not in user_dict_new:
    print 'user not'
else:
    password_new=raw_input('���������룺')
    user_dict_new[username_new]=password_new
    print user_dict_new
    f=open('user.txt','w+')
    for k,y in user_dict_new.items():
        #print user_dict_new.items()
        #print k,y
        f.write(k+':'+y+'\n')
    f.close()

