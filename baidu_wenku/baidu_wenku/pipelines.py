# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import datetime
import json
import os
import time

class BaiduWenkuPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __init__(self):
        self.year = str(datetime.datetime.now().year)
        self.month = str(datetime.datetime.now().month)
        self.day = str(datetime.datetime.now().day)
        self.hour = str(datetime.datetime.now().hour)
        self.file_1 = os.path.join('data', '{}'.format('baidu_wenku_{}.json'.format(int(time.time()))))

    def process_item(self, item, spider):
        if not os.path.exists('data'):
            os.makedirs('data')
        self.file = codecs.open(self.file_1, 'a', encoding="utf-8")
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
