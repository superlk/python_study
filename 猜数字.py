#!/usr/bin/env python
#_*_coding:utf-8_*_
import random
shuzi=random.randint(0,10)
print '��������Ϸ������3�λ���'
print shuzi
count =0
while count <3:
   count+=1
   num=input('����������(1-10֮��):')
   if num==shuzi:
       print '��ϲ��¶���'
       break
   elif num>shuzi:
       print '��´���,�㻹��%s�λ���'%(3-count)
   else:
       print '���С�ˣ��㻹��%s����'%(3-count)
print '��Ϸ����'