#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'd_c0="AJCC0XpdYguPTu90oFuW1yCHzIYHDkFwRdU=|1488359734"; _zap=0eeb9ece-4a5a-470b-a511-c191cee62216; q_c1=6c402e4c2078468ab6e4f2f94d8b8828|1493950122000|1488359734000; _xsrf=c62a33df251e43601f920356b01c117a; aliyungf_tc=AQAAAEl4p2V8Bw8AEIF3AYO0H61V/H+k; acw_tc=AQAAAGCOriCwJQEAEIF3AdYXUjIMpjto; r_cap_id="OTNkNDdiMGY1NWEyNDU4MmJhYTU4MjJjNmU2ODRlNDM=|1495013004|898f0f7f3c2c5654796088f6ff6ad0b70469a5c5"; cap_id="MzlmYTlhYzUxM2M0NGIwNTk4YWRjYzg0M2M5ODc3OWY=|1495013004|2df52013fc5975fcb2d0261db6c58d468b78ef66"; l_n_c=1; z_c0=Mi4wQUVDQWlNc0Z0d29Ba0lMUmVsMWlDeGNBQUFCaEFsVk5sYU5EV1FCQ1YzdjlIdzNiWHk4SktCb0I2VTE5dVN2YkFR|1495015351|bc055dbef07c8c7f252643ee09333096d1b074c9; __utma=51854390.1738281953.1488359723.1495013002.1495015350.14; __utmb=51854390.0.10.1495015350; __utmc=51854390; __utmz=51854390.1495015350.14.12.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/zhang-sir-76-99/following/columns; __utmv=51854390.100--|2=registration_date=20161019=1^3=entry_date=20161019=1',
    'Host': 'www.zhihu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

r = requests.get('https://www.zhihu.com/people/zhang-sir-76-99/following/columns', headers=headers)
r.encoding = 'utf-8'
print(r.text)
