#!/usr/bin/env python
#_*_coding:utf-8_*_
#λ�ò���
'''
from test.test_support import args_from_interpreter_flags
def hello(name='lk',job='it'):
    return 'my name is %s,my job is %s'%(name,job)
print hello('xiaoming','linux')
print hello('linux','xiaoxiao')

#�ؼ��ֲ���
print hello(name='ll',job='python')
print hello(job='python', name='ll')

def hoo(name,*args,**kargs):
    print name,args,kargs
hoo(1,2,3,4,5,6,7,c=4)
hoo('lk',a=2,b=3)
'''
def hello(ip,status):
    print ip+':'+status
    
res=[['192.1','200'],['192.2','404'],['192.3','500']]
for r in res:
    hello(*r)  #*���ڵ���ʱ�򣬿�����Ϊ��listչ������ֵ������
    hello(r[0], r[1])
#**�ڵ��õ�ʱ�򣬿��԰�dictչ�������ɹؼ��ֲ���
res_dict=[{'ip':'111','status':'100'},{'ip':'222','status':'200'}]
for r in res_dict:
    hello(**r)