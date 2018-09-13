# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import datetime
import json
import time
import os
import random
import socket
import string
from scrapy.exceptions import DropItem


class JsonWriterPipeline(object):
    def __init__(self):
        self.year = str(datetime.datetime.now().year)
        self.month = str(datetime.datetime.now().month)
        self.day = str(datetime.datetime.now().day)
        self.hour = str(datetime.datetime.now().hour)
        self.file_path_1 = os.path.join('data', '{:0>2}'.format(self.year), '{:0>2}'.format(self.month),
                                        '{:0>2}'.format(self.day))
        self.file_1 = os.path.join(self.file_path_1,
                                   '{}'.format('cs_com_data_{}_{}.json'.format(self.get_host_ip(), int(time.time()))))

    def get_host_ip(self):
        ip_raw = ''
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip_raw = s.getsockname()[0]
            ip = '_'.join(ip_raw.split('.'))
        finally:
            s.close()
            if not ip_raw:
                ip = random_str
        return ip

    def process_item(self, item, spider):
        if not item['title']:
            raise DropItem('Missing title ')
        item['source'] = item['source'].replace(u'来源：', '')
        item['author'] = item['author'].replace(u'作者：', '')
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        if not os.path.exists('{}'.format(self.file_path_1)):
            os.makedirs(self.file_path_1)
        self.file = codecs.open(self.file_1, 'a', encoding="utf-8")
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class CsComPipeline(object):
    def process_item(self, item, spider):
        return item
