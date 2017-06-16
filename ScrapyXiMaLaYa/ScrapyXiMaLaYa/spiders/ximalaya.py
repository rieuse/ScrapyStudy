# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ScrapyXiMaLaYa.items import ScrapyximalayaItem


class XimalayaSpider(scrapy.Spider):
    name = "ximalaya"
    allowed_domains = ["ximalaya.com"]
    # start_urls = ['http://www.ximalaya.com/dq/all/']
    start_urls = ['http://www.ximalaya.com/dq/all/{}'.format(num) for num in range(1, 5)]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        for content in soup.find_all(class_="albumfaceOutter"):
            item = ScrapyximalayaItem()
            item['url'] = content.a['href']
            item['title'] = content.img['alt']
            item['img_url'] = content.img['src']
            yield item
