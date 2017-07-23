#!/usr/bin/env python
#_*_coding:utf-8_*_
import random
shuzi=random.randint(0,10)
print '猜数字游戏，你有3次机会'
print shuzi
count =0
while count <3:
   count+=1
   num=input('请输入数字(1-10之间):')
   if num==shuzi:
       print '恭喜你猜对了'
       break
   elif num>shuzi:
       print '你猜大了,你还有%s次机会'%(3-count)
   else:
       print '你猜小了，你还有%s机会'%(3-count)
print '游戏结束'