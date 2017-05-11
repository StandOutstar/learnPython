#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

# 有的网站没有header是会被禁止的
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
params = {}
html = requests.get("http://www.qqdna.com/forum-45-1.html").text

# print(html)
# title = re.search('<title>(.*?)</title>', html, re.S).group(1)
# print(title)
# print(type(title))

link = re.findall('<td class="num"><a href="(.*?)" class="xi2"', html, re.S)
print(type(link))
count = 0
for each in link:
    print(each)
    count += 1

print(count)

# text_filed = re.findall('class="common">(.*?)<th>', html, re.S)
# print(text_filed)
# for each in text_filed:
#     link = re.findall('href="(.*?)".onclick', each, re.S)
#     print(link)
