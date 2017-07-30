#!/usr/bin/env python
#_*_coding:utf-8_*_
# 判断登陆用户是否在列表中。
# 如果用户存在，则判断密码是否一致，
# 如何用户存在，则判断密码是否正确
# 如何密码真确，打印客户信息
users = [{'age': 18, 'job': 'coo', 'name': 'wd', 'passwd': '12323'},
 {'age': 19, 'job': 'cto', 'name': 'kk', 'passwd': 'abcdef'},
 {'age': 20, 'job': 'cio', 'name': 'pc', 'passwd': 'ABC'}]


name=raw_input('请输入你的用户名：')
for i in range(len(users)):
#    print users[i]['name']
    if name ==users[i]['name']:
        pwd=raw_input('请输入密码：')
        if pwd==users[i]['passwd']:
            print users[i]
            break
        else:
            print '密码错误'
            break
        
else:
    print '用户名不存在'


#方法2
name_list=[]
passwd_lsit=[]

for i in users:
    name_list.append(i['name'])
    passwd_lsit.append(i['passwd'])
name=raw_input('输入用户名：')
if name in name_list:
    pwd=raw_input('输入密码：')
    if pwd==passwd_lsit[name_list.index(name)]:
        print users[name_list.index(name)]
    else:
        print 'passwd error'
else:
    print 'name error' 
    