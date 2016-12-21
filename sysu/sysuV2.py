#coding=utf-8
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://cas.sysu.edu.cn/cas/login?service=http://ecampus.sysu.edu.cn/zsuyy/login.jsp')
elemUsername = driver.find_element_by_name('username')
elemPassword = driver.find_element_by_name('password')
elemUsername.send_keys('liujihui')
elemPassword.send_keys('86575501')
driver.find_element_by_name("submit").click()
driver.get('http://ecampus.sysu.edu.cn/zsuyy/yanyuan/xj/studentmng.do?method=getStudentMajorList')
print driver.page_source.encode('utf-8')
#我的学籍
f = open('getStudentMajorList.html','w')
f.write(driver.page_source.encode('utf-8'))
f.close()

