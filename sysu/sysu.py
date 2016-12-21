
# -*- coding: utf-8 -*-

import requests
import urllib2
from urllib import urlencode
import time
import os
from bs4 import BeautifulSoup as bs
from cookielib import LWPCookieJar
import  json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
hostUrl = 'https://cas.sysu.edu.cn'
#获取提交表单form中的input元素:lt,-eventId,submit,exection
def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''
    soup = bs(str,'lxml')
    tt = {}
    tt['action'] = hostUrl + soup.form['action']
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            if(inp.get('name')=='lt'):
                tt['lt'] =inp.get('value')
            if(inp.get('name')=='execution'):
                tt['execution'] = inp.get('value')
            if (inp.get('name') == '_eventId'):
                tt['_eventId'] = inp.get('value')
            if (inp.get('name') == 'submit'):
                tt['submit'] = inp.get('value')
    return tt

# 创建会话对象,同一个session之间会保持cookie
s = requests.Session()
# 将cookie保存到cookiejar文件中,方便以后使用
s.cookies = LWPCookieJar('cookiejar')
r = s.get("https://cas.sysu.edu.cn/cas/login?service=http://ecampus.sysu.edu.cn/zsuyy/login.jsp")
soup = toJson(r.text)
payload ={'username':'*******','password':'*******','lt':soup["lt"],'execution':soup['execution'],'_eventId':'submit','submit':'%E7%99%BB%E5%BD%95'}
postUrl = soup['action']
posts = s.post(postUrl,data = payload)
s.cookies.save(ignore_discard=True)


stdConfirmInfoUrl = 'http://ecampus.sysu.edu.cn/zsuyy/yanyuan/xj/studentmng.do?method=stdConfirmInfoPage'
scoresUrl = 'http://ecampus.sysu.edu.cn/zsuyy/yanyuan/py/pychengji.do?method=enterChaxun'
lessonsUrl = 'http://ecampus.sysu.edu.cn/zsuyy/yanyuan/py/pyjxjh.do?method=enter'
#学生信息页面抓取
stdConfirmInfo = s.get(stdConfirmInfoUrl)
f = open('stdConfirmInfo.html','w')
f.write(stdConfirmInfo.text.encode('utf-8'))
f.close()
#成绩页面
scores = s.get(scoresUrl)
f = open('scores.html','w')
f.write(scores.text.encode('utf-8'))
f.close()
#课程页面
lessons = s.get(lessonsUrl)
f = open('lessons.html','w')
f.write(lessons.text.encode('utf-8'))
f.close()

