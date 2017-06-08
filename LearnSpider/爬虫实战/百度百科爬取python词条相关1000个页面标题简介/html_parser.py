#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import urllib.parse
# from os import path
# log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging_config.ini')
# fileConfig(log_file_path)
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger=logging.getLogger('infoLogger')
logger_error=logging.getLogger('errorLogger')
# logger.info('test1')
# logger_error.error('test2')


class HtmlParser(object):
    #   python词条url: http://baike.baidu.com/item/Python
    #   相关url: /item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80
    #   相关url 位置：<a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>
    #   title: <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
    #   summary: <div class="lemma-summary" label-module="lemmaSummary">
    def html_parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = []
        # /item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80
        links = soup.find_all('a', href=re.compile(r'/item/\w*'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.append(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        #   title: <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #   summary: <div class="lemma-summary" label-module="lemmaSummary">
        new_data = {'url': page_url, 'title': soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1').get_text(),
                    'summary': soup.find('div', class_="lemma-summary").get_text()}

        return new_data

if __name__ == '__main__':
    r = requests.get('http://baike.baidu.com/item/Unix%20shell')
    r.encoding = 'utf-8'
    hh = HtmlParser()
    newurl, newdata = hh.html_parse('http://baike.baidu.com/item/Unix%20shell', r.text)
    print(newurl)
    print(newdata)
