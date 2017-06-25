# -*- coding: utf-8 -*-
import scrapy
from Guoke.items import GuokeItem


class GuokeSpider(scrapy.Spider):
    name = "guoke"
    allowed_domains = ["guokr.com"]
    start_urls = ['http://www.guokr.com/ask/hottest/?page={}'.format(n) for n in range(1, 8)] + [
        'http://www.guokr.com/ask/highlight/?page={}'.format(m) for m in range(1, 101)]

    def parse(self, response):
        item = GuokeItem()
        i = 0
        for content in response.xpath('/html/body/div[3]/div[1]/ul[2]/li'):
            item['title'] = content.xpath('//div[2]/h2/a/text()').extract()[i]
            item['Focus'] = content.xpath('//div[@class="ask-hot-nums"]/p[1]/span/text()').extract()[i]
            item['answer'] = content.xpath('//div[1]/p[2]/span/text()').extract()[i]
            item['link'] = content.xpath('//div[2]/h2/a/@href').extract()[i]
            item['content'] = content.xpath('//div[2]/p/text()').extract()[i]
            i += 1
            yield item