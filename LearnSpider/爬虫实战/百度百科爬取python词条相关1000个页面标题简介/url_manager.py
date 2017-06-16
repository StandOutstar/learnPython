#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger=logging.getLogger('infoLogger')
logger_error=logging.getLogger('errorLogger')

# url管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        # 避免重复查询
        self.old_urls = set()

    # 可变参数，可添加一个，也可批量添加
    def add_new_urls(self, *urls):
        if urls is None or len(urls) == 0:
            return
        else:
            for url in urls:
                if url not in self.new_urls and url not in self.old_urls:
                    self.new_urls.add(url)

    def has_new_url(self):
        if len(self.new_urls) != 0:
            return True
        return False

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


if __name__ == '__main__':
    c = UrlManager()
    urls = []
    urls.append('123')
    urls.append('456')
    c.add_new_urls('123', '456')
    print(c.new_urls)
