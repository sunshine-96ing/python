import requests

import requests.packages

'''response = requests.get('https://www.baidu.com/')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
'''

'''
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/head')
requests.options('http://httpbin.org/options')
'''

'''
response = requests.get('http://httpbin.org/get')
print(response.text)
'''

'''
data = {
    'name':'hujing',
    'age':22
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)

response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(type(response.json()))
'''

'''response = requests.get('http://github.com/favicon.ico')
print(type(response.text),type(response.content))
print(response.text)
print(response.content)
with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()
'''
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
}
# 添加headers
'''
headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
}
response = requests.get('http://www.zhihu.com/explore',headers=headers)
print(response.text)
'''

# 基本POST请求
data = {'name': 'hujing', 'age': '22'}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(response.text)

'''
response = requests.get('http://www.jianshu.com')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)
'''

# 状态码判断
# response = requests.get('http://www.jianshu.com/hello.html')
# exit() if not response.status_code ==  requests.codes.ok else print('Request Successfully')

# 高级操作

'''#文件上传
files = {
    'file':open('favicon.ico','rb')
}
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)
'''

# response = requests.get('https://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+'='+value)

requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

# 证书
response = requests.get('https://www.12306.cn')
print(response.status_code)

requests.packages.urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
# print(response.status_code)

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'https://127.0.0.1:10809',
}
response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)

proxies = {
    'http': 'http://user:password@127.0.0.1:10809/',
}
response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)

response = requests.get('https://www.taobao.com',timeout = 1)
print(response.status_code)

# from requests.auth import HTTPBasicAuth
# r = requests.get('http://120.27.34.24:9001',auth = HTTPBasicAuth('user','123'))
# print(response.status_code)

from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response = requests.get('http://httpbin.org/get',timeout = 0.1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')