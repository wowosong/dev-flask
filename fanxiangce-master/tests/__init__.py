# -*-coding: utf-8-*-
from selenium import  webdriver
from time import  sleep
wd=webdriver.Chrome()
wd.get('http://www.baidu.com')
wd.close()