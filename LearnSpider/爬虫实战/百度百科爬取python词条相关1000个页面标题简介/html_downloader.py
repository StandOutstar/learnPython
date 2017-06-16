#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger=logging.getLogger('infoLogger')
logger_error=logging.getLogger('errorLogger')


# 网页下载器
class HtmlDownloader(object):
    def html_download(self, url):
        if url is None:
            logger_error.error('url is none')
            return None
        response = requests.get(url)
        if response.status_code != 200:
            logger.warning('get response fail code %s' % response.status_code)
            return None
        encode = re.findall(r'<meta charset="(.*?)">', response.text)
        logger.info(encode)
        response.encoding = encode[0]
        return response.text


if __name__ == '__main__':
    do = HtmlDownloader()
    text = do.html_download('http://baike.baidu.com/item/Python')
    print(text)
