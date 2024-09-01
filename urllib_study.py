#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from selenium import webdriver
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import socket

response = requests.get('http://www.baidu.com')

# print(response.text)
# print(response.headers)
# print(response.status_code)

headers = {}
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
# response = requests.get('http://www.baidu.com', headers=headers)
# print(response.headers)
# chrome_driver = r"D:\python_workspace\hello_word\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver)
# driver.get('http://m.weibo.com')
# driver.get('http://www.zhihu.com')
# driver.get('http://www.taobao.com')
# print(driver.page_source)
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')
# 响应
response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.read().decode('utf-8'))

# url = 'http://httpbin.org/post'
# data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# Handler
# 代理
# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://127.0.0.1:10809',
#     'https': 'https://127.0.0.1:10809',
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

# Cookie
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.taobao.com')
# for item in cookie:
# print(item.name+"="+item.value)

# try:
# #     response = urllib.request.urlopen('http://hujing.org/index.htm')
# # except urllib.error.URLError as e:
# #     print(e.reason)

# try:
#     response = urllib.request.urlopen('http://www.hujing.com/index.htm')
# except urllib.error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sop='\n')
# except urllib.error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result)
#
# result = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)
#
# result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)
#
# result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
# print(result)
#
# result = urllib.parse.urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
# print(result)

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urllib.parse.urlunparse(data)) #http://www.baidu.com/index.html;user?a=6#comment

params = {
    'name':'germey',
    'age':'22'
}
# base_url = 'http://www.baidu.com?'
# url = base_url+urllib.parse.urlencode(params)
print(url) #http://www.baidu.com?name=germey&age=22
