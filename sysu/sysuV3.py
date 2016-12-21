# -*- coding: utf-8 -*-
import  cookielib
import  urllib
import  urllib2
import requests
from urllib import urlencode
import time
import os
from bs4 import BeautifulSoup as bs
import  json
hostUrl = 'https://cas.sysu.edu.cn'
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
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
#if not os.path.exists('cookiejar'):
#如果没有cookie就post一下获取cookie,否则直接用本地文件中保存好的cookie
response = opener.open('https://cas.sysu.edu.cn/cas/login?service=http://ecampus.sysu.edu.cn/zsuyy/login.jsp')
soup = toJson(response.read())
payload =urllib.urlencode({'username':'liujihui','password':'86575501','lt':soup["lt"],'execution':soup['execution'],'_eventId':'submit','submit':'%E7%99%BB%E5%BD%95'})
postUrl = soup['action']
result = opener.open(postUrl,payload)
cookie.save(ignore_discard=True, ignore_expires=True)
stdConfirmInfoUrl = 'http://ecampus.sysu.edu.cn/zsuyy/yanyuan/xj/studentmng.do?method=stdConfirmInfoPage'
#学生信息页面抓取
#else:
#   print "cookie exists,restore"
#   cookie.load(ignore_discard=True)
stdConfirmInfo = opener.open(stdConfirmInfoUrl)
f = open('12.html','w')
f.write(stdConfirmInfo.read())
f.close()
