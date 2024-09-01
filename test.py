#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import datetime;

import requests
import schedule  # 此模块用于计划任务
import yagmail  # 此模块用于发邮件
from bs4 import BeautifulSoup

ran = 0
url = 'https://tianqi.2345.com/gongshu1d/71853.htm'  # 定义天气预报的url
loveurl = 'https://www.guaze.com/juzi/23389.html'  # 定义情话的url


def email():
    global ran  # 将ran变量声明为全局变量
    web = requests.get(url)
    # print(web.text)

    page = BeautifulSoup(web.text, "html.parser")

    # print(ran)

    # print(love[ran])

    weather = page.find("div", class_="real-today")

    info = []
    for li_tag in page.find_all('ul', {'class': 'real-data'}):
        for lis in li_tag.find_all('li'):
            for elem in lis:
                if len(elem.text.strip()) != 0:
                    info.append(elem.text.strip())

    other_info = "\n".join(str(i) for i in info)
    # print(other_info)
    # print(weather.text)

    air = "今天空气质量:" + page.find("div", class_="aqi-map-con").text.replace("\n", "\t")

    one_text = page.find("div", class_="aqi-map-tb").find("p", class_="aqi-map-type").text

    air_info = []
    for li_tag in page.find_all('ul', {'class': 'aqi-map-tf'}):
        for lis in li_tag.find_all('li'):
            for elem in lis:
                if len(elem.text.strip()) != 0 and elem.text.strip() != '不用佩戴口罩':
                    air_info.append(elem.text.strip())
    air_other_info = "\t".join(str(i) for i in air_info)

    # 每日一句
    # web2 = requests.get(loveurl)
    # web2.encoding = 'gb2312'
    # page = BeautifulSoup(web2.text, "html.parser")
    #
    # div = page.find('div', class_="content")
    #
    # div = str(div.text)
    # # print(div)
    # grep = re.compile(r"\d+、(.*)")
    # content = grep.findall(div)
    # print(content)

    resp = requests.get('https://v1.hitokoto.cn/', params={'encode': 'text'})

    # email函数内的内容是爬取天气和情话的，具体的地址天气你可以更换url

    yag = yagmail.SMTP(
        host='smtp.163.com', user='15372026611@163.com',  # 如过用的是qq邮箱就写smtp.qq.com，如果是163就写smtp.163.com
        password='BIQMBCIMAKOFGVFM', smtp_ssl=True  # 授权码在qq邮箱里开启smtp就会生成一个
    )
    # weather = ["杭州市拱墅区:", weather.text, other_info, air + "," + one_text, air_other_info, "每日一句:", content[ran],
    #            # 定义发送内容
    #            # yagmail.inline(r"./love.jpg")    # 附件图片，不发图片可以删掉
    #            ]
    weather = ["杭州市拱墅区:", weather.text, other_info, air + "," + one_text, air_other_info, "每日一句:", resp.text,
               # 定义发送内容
               # yagmail.inline(r"./love.jpg")    # 附件图片，不发图片可以删掉
               ]
    yag.send(
        to=['15372026611@163.com'],
        subject='天气预报',  # 邮件主题
        contents=weather  # 发送的内容为上面定义的weather，其中weather.text是天气预报，content[ran]是情话
    )

    yag.send(
        to=['864324268@qq.com'],
        subject='00专属天气预报来啦！',  # 邮件主题
        contents=weather  # 发送的内容为上面定义的weather，其中weather.text是天气预报，content[ran]是情话
    )
    print(datetime.datetime.now(), "发送完成")
    print("发送完成")
    ran += 1


schedule.every().day.at("00:30").do(email)      # 每天5点21分执行函数email0
# schedule.every(10).seconds.do(email)  # 每10秒执行一下函数email的内容
#
# ，我这里用于测试
while True:
    schedule.run_pending()

if __name__ == '__main__':
    email()
