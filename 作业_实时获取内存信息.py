#!/usr/bin/env python
#_*_coding:utf-8_*_

# 格式化输出
def formatNum(num):
    num=int(num)
    o='KB'
    if num>1024*1024:
        num/=(1024*1024)
        o='GB'
    elif num>1024:
        num/=1024
        o='MB'
    return '%.2f%s'%(num,o)

# 格式化
def get_mem_info(arr):
    tmp=arr.split()
    tmp[1]=formatNum(tmp[1])
    return tmp[:2]

# 处理文件
def operate(key):
    with open('/proc/meminfo') as f:
        mem_total=key(f.readline())
        mem_free=key(f.readline())
        mem_ava=key(f.readline())
        mem_buf=key(f.readline())
        mem_cache=key(f.readline())
        '''
        print f.readline().split()[:2]
        print f.readline().split()[:2]
        print f.readline().split()[:2]
        print f.readline().split()[:2]
        '''
        return[mem_total,mem_free,mem_ava,mem_buf,mem_cache]

# 写入html
def get_html(arr):
    html_str='<table border=1>'
    for mem in arr:
        html_str+='<tr><td>%s</td><td>%s</td></tr>'%tuple(mem)
    html_str+='</table>'
    with open('mem.html','w') as f:
        f.write(html_str)
# 入口        
def getMem():
    mem_info=operate(get_mem_info)
    get_html(mem_info)

getMem()
    
        