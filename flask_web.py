#!/usr/bin/env python
#_*_coding:utf-8_*_

# 导入Flask类
from flask import Flask
# 新建app，内容都是写死的
app=Flask(__name__)

# 定义一个url，今天/目录
@app.route('/')
# 定义一个函数，当访问这个目录时，会触发这个函数
def index():
    # 返回值会在浏览器里
    return 'hello world'
@app.route('/lk')
def lk():
    print 'lklk'

if __name__=='__main__':
    # 应用跑起来，允许所有ip访问，要不只能本机访问.端口9092,debug开启调试模式
    app.run(host='0.0.0.0'，port='9092' debug=True)