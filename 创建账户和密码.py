#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
#确定文件里是否有用户名，如果没有创建，
while True:
    username=raw_input('创建账户')
    f=open('user.txt')
    user_dict={}
    arr=f.read().split('\n')
    for  line in  arr:
        if line:   #如果不为空
            temp=line.split(':')
            user_dict[temp[0]]=temp[1]
            print user_dict
    f.close()
    
    if username in user_dict:
        print 'user exists'
    else:
        password=raw_input('输入密码')
        f=open('user.txt','a')
        f.write('\n'+username+':'+password)
        f.close()
        break
'''
#修改密码怎么写
# 输入用户名，如果有，修改密码，如果没有，报错
print'-'*10,'修改密码','-'*10
user_dict_new={}
username_new=raw_input('输入你的用户名：')
f=open('user.txt')
for  line in  f.read().split('\n'):
    if line:   #如果不为空
        temp_new=line.split(':')
        user_dict_new[temp_new[0]]=temp_new[1]
print user_dict_new
f.close()
if username_new not in user_dict_new:
    print 'user not'
else:
    password_new=raw_input('输入新密码：')
    user_dict_new[username_new]=password_new
    print user_dict_new
    f=open('user.txt','w+')
    for k,y in user_dict_new.items():
        #print user_dict_new.items()
        #print k,y
        f.write(k+':'+y+'\n')
    f.close()

