#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 目标：爬取python词条相关1000个页面
# 目标分析：
#   python词条url: http://baike.baidu.com/item/Python
#   相关url: /item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80
#   相关url 位置：<a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>
#   title: <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
#   summary: <div class="lemma-summary" label-module="lemmaSummary">
import html_downloader
import html_outputer
import html_parser
import url_manager
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger=logging.getLogger('infoLogger')
logger_error=logging.getLogger('errorLogger')


# 调度器
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_urls(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                logger.info('Craw %d url: %s' % (count, new_url))
                html_cont = self.downloader.html_download(new_url)
                new_urls, new_data = self.parser.html_parse(new_url, html_cont)
                self.urls.add_new_urls(*new_urls)
                self.outputer.collectdata(new_data)

                if count >= 1000:
                    break

                count += 1
            except Exception as e:
                logger_error.error(e)
                logger_error.error('craw filed %s' % new_url)
        self.outputer.output()


if __name__ == '__main__':
    # root_url = 'http://baike.baidu.com'
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
