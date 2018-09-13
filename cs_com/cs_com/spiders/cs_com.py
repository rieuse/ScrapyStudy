# -*- coding: utf-8 -*-
import datetime
import logging
import os
import sys
import scrapy
from scrapy import Request
from ..items import CsComItem
from ..settings import cs_com_start_urls
from ..utils import url_skip
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except:
    pass

class CsComSpiderSpider(scrapy.Spider):
    name = 'cs_com'
    allowed_domains = ['cs.com.cn']
    start_urls = cs_com_start_urls

    def __init__(self):
        self._year = str(datetime.datetime.now().year)
        self._month = str(datetime.datetime.now().month)
        self._day = str(datetime.datetime.now().day)
        self._hour = str(datetime.datetime.now().hour)
        self._yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d")
        file_name = '_SUCCESS'
        file_path = os.path.join('data', '{:0>2}'.format(self._year), '{:0>2}'.format(self._month),
                                 '{:0>2}'.format(self._yesterday))
        try:
            file_num = len(os.listdir(file_path))
            if file_num >0:
                if not os.path.exists(os.path.join('{}'.format(file_path), '{}'.format(file_name))):
                    file = open(os.path.join('{}'.format(file_path), '{}'.format(file_name)), 'w')
                    file.close()
        except:
            pass

    def parse(self, response):
        self.today = datetime.datetime.now().date()
        self.yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
        # 获取全部文章的链接
        article_urls_raw = response.xpath('/html/body/div/div[1]/ul/li/a/@href').extract()
        article_urls = [url_skip(response.url,raw_url) for raw_url in article_urls_raw]
        # logging.debug(article_urls)
        # 特殊板块不需要url跳转修改
        if 'cj/zt' in response.url or 'zzqh/qhzk' in response.url:
            article_urls = article_urls_raw
        # 截取昨天的文章链接
        article_times = response.xpath('/html/body/div/div[1]/ul/li/span/text()').extract()
        today_nums = len([i for i in article_times if datetime.datetime.strptime(i, '%y-%m-%d %H:%M').date() == self.today])
        yesterday_nums = len([i for i in article_times if datetime.datetime.strptime(i, '%y-%m-%d %H:%M').date() == self.yesterday])
        yesterday_urls = article_urls[today_nums:today_nums+yesterday_nums]
        # logging.info('url:{},\n num:{}'.format(response.url,yesterday_nums))
        # 查看下一页数据有没有需要抓取的
        if not yesterday_urls or yesterday_nums + today_nums == 33:
            next_page_url = ''
            if 'index.shtml' in response.url:
                next_page_url = response.url.replace('index','index_1')
            for i in range(1,10):
                if str(i) in response.url:
                    next_page_url = response.url.replace(str(i),str(i+1))
                    break
            yield Request(next_page_url, callback=self.parse)
        for url in yesterday_urls:
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = CsComItem()
        item['title'] = response.xpath('/html/body/div/div[1]/div[2]/h1/text()').extract_first('')
        item['time'] = response.xpath('/html/body/div/div[1]/div[2]/div[1]/p[2]/em[1]/text()').extract_first('')
        item['link'] = response.url
        item['source'] = response.xpath('/html/body/div/div[1]/div[2]/div[1]/p[2]/em[2]/text()').extract_first('')
        item['author'] = response.xpath('//*[@class="info"]/p/text()').extract_first('')
        item['content'] = response.xpath('//div[@class="article-t hidden"]/*/text()').extract()
        item['content'] = ''.join(response.xpath('//div[@class="article-t hidden"]/p/text()').extract())
        try:
            content_time = datetime.datetime.strptime(item['time'], '%Y-%m-%d %H:%M').date()
        except:
            content_time = datetime.datetime.strptime(item['time'], '%y-%m-%d %H:%M').date()
        if '国家统计局' in item['source']:
            logging.info('tongjijiP{}'.format(response.url))
            item['content'] = ''.join(response.xpath('//div[@class="article-t hidden"]/p/span/text()').extract())
        if not item['title']:
            logging.info('no title')
        # 如果文章不是昨天的，不保存
        elif content_time != self.yesterday:
            logging.info('time is not right time: {}'.format(content_time))
        else:
            yield item

    def close(self, spider, reason):
        file_name = '_SUCCESS'
        file_path = os.path.join('data','{:0>2}'.format(self._year),'{:0>2}'.format(self._month),'{:0>2}'.format(self._day))
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file = open(os.path.join('{}'.format(file_path),'{}'.format(file_name)), 'w')
        file.close()
