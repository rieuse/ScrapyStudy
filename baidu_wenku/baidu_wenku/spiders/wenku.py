# -*- coding: utf-8 -*-
import codecs

import scrapy
from urllib.parse import quote
from ..items import BaiduWenkuItem


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']


    def start_requests(self):
        f = codecs.open('query.txt','r',encoding='utf-8')
        for line in f.readlines():
            words = line.split('/')
            for word in words:
                url = 'https://baike.baidu.com/item/{}'.format(quote(word.strip()))
                yield scrapy.Request(url=url, callback=self.parse)
        f.close()


    def parse(self, response):
        if not response.status == 302:
            item = BaiduWenkuItem()
            item['summary'] = response.xpath('//*[@id="J-lemma"]/div[3]/div[1]/div[4]/div[2]/p/text()').extract_first()
            introduce_title = response.xpath('//*[@id="J-basicInfo"]/ul/li/div[1]/text()').extract()
            introduce_content = response.xpath('//*[@id="J-basicInfo"]/ul/li/div[2]/text()').extract()
            item['introduce'] = [i.strip()+':'+j.strip() for i,j in zip(introduce_title,introduce_content)]
            business_circles_title = response.xpath('//*[@id="J-enterpriseInfo"]/div[2]/dl/dt/text()').extract()
            business_circles_content = response.xpath('//*[@id="J-enterpriseInfo"]/div[2]/dl/dd/text()').extract()
            item['business_circles'] = [i.strip()+j.strip() for i,j in zip(business_circles_title,business_circles_content)]
            yield item
