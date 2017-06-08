#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger=logging.getLogger('infoLogger')
logger_error=logging.getLogger('errorLogger')


class HtmlOutputer(object):
    def __init__(self):
        self.new_data = []

    def collectdata(self, new_data):
        if new_data is None:
            return
        self.new_data.append(new_data)

    def output(self):
        with open('output.html', 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table border="1">')
            for data in self.new_data:
                fout.write('<tr>')
                fout.write('<td>%s</td>' % data['url'])
                fout.write('<td>%s</td>' % data['title'])
                fout.write('<td>%s</td>' % data['summary'])
                fout.write('</tr>')
            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
        pass

if __name__ == '__main__':
    ht = HtmlOutputer()
    ht.collectdata({'url': 123, 'title': 'python', 'summary': 'qweerrtrtyrydfg'})
    ht.collectdata({'url': 456, 'title': 'python123', 'summary': 'qweerrtrtyrydfg'})
    ht.output()
