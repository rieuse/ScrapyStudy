# -*- coding: utf-8 -*-
import scrapy
from ShiXiSeng.items import ShixisengItem
from scrapy import Request


class ShixiSpider(scrapy.Spider):
    name = "shixi"
    allowed_domains = ["shixiseng.com"]
    start_urls = ['http://www.shixiseng.com/interns?p=1']
    headers = {
        'Host': 'www.shixiseng.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://www.shixiseng.com',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept - Language': 'zh-CN,zh;q=0.8,en;q=0.6'
    }

    def parse(self, response):
        links = response.xpath('//div[@class="po-name"]/div[1]/a/@href').extract()
        for link in links:
            dlink = 'http://www.shixiseng.com' + link
            yield Request(dlink, meta={'link': dlink}, headers=self.headers, callback=self.parser_detail)

    def parser_detail(self, response):
        item = ShixisengItem()
        item['name'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/span[1]/span/text()').extract_first()
        item['link'] = response.meta['link']
        item['company'] = response.xpath('//*[@id="container"]/div[1]/div[2]/div[1]/p[1]/a/text()').extract_first()
        item['place'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/span[2]/@title').extract_first()
        item['education'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/span[3]/text()').re_first(
            r'[\u4e00-\u9fa5]{2}')
        item['people'] = response.xpath('//*[@id="container"]/div[1]/div[2]/div[1]/p[2]/span/text()').extract()[1]
        item['money'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/span[1]/text()').re_first(r'[^\s]+')
        item['week'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/span[4]/text()').extract_first()
        item['month'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/span[5]/text()').extract_first()
        item['lure'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/p/text()').extract_first()
        item['description'] = response.xpath(
            '//div[@class="dec_content"]/*/text()|//div[@class="dec_content"]/text()').extract()
        item['data'] = response.xpath('//*[@id="container"]/div[1]/div[1]/p[3]/text()').extract()
        yield item