#!/usr/bin/env python
#_*_coding:utf-8_*_

# ����Flask��
from flask import Flask
# �½�app�����ݶ���д����
app=Flask(__name__)

# ����һ��url������/Ŀ¼
@app.route('/')
# ����һ�����������������Ŀ¼ʱ���ᴥ���������
def index():
    # ����ֵ�����������
    return 'hello world'
@app.route('/lk')
def lk():
    print 'lklk'

if __name__=='__main__':
    # Ӧ������������������ip���ʣ�Ҫ��ֻ�ܱ�������.�˿�9092,debug��������ģʽ
    app.run(host='0.0.0.0'��port='9092' debug=True)