# -*- coding: utf-8 -*-
import scrapy
from Guoke.items import GuokeItem
from scrapy import Request


class GuokeSpider(scrapy.Spider):
    name = "guokedetail"
    allowed_domains = ["guokr.com"]
    # start_urls = ['http://www.guokr.com/ask/hottest/']
    start_urls = ['http://www.guokr.com/ask/hottest/?page={}'.format(n) for n in range(1, 8)] + [
        'http://www.guokr.com/ask/highlight/?page={}'.format(m) for m in range(1, 101)]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie':'_32382_access_token=6b39c2b731b36ff39a5a5ff288cfef9b04e35c7f2e1986c8f20c1399bd441791; _32382_ukey=mqhvi4; _32382_auto_signin=1; _32353_access_token=878f286937f647ddcd5cb08e6fa5e3ed9bb2a084380dbd274de9cb3d7f7bbbd4; _32353_ukey=mqhvi4; _32353_auto_signin=1; isN=1; support=1; session=46f4aea6-7af4-4749-8fbe-29670eab53b2',
        'Host': 'www.guokr.com',
        # 'Referer':'http://www.guokr.com/ask/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    def parse(self, response):
        items = {}
        i = 0
        for content in response.xpath('/html/body/div[3]/div[1]/ul[2]/li'):
            items['title'] = content.xpath('//div[2]/h2/a/text()').extract()[i]
            items['Focus'] = content.xpath('//div[@class="ask-hot-nums"]/p[1]/span/text()').extract()[i]
            items['answer'] = content.xpath('//div[1]/p[2]/span/text()').extract()[i]
            items['link'] = content.xpath('//div[2]/h2/a/@href').extract()[i]
            i += 1
            yield Request(items['link'], meta={'title': items['title'], 'link': items['link'], 'Focus': items['Focus'],
                                               'answer': items['answer']}, headers=self.headers,
                          callback=self.parser_detail)
            # yield item

    def parser_detail(self, response):
        item = GuokeItem()
        item['title'] = response.meta['title']
        item['Focus'] = response.meta['Focus']
        item['answer'] = response.meta['answer']
        item['link'] = response.meta['link']
        pa = []
        answer = response.xpath('//*[@id="answers"]/div[2]/div[2]/div[3]/p/text()')
        for i in answer:
            pa.append(i.extract())
        item['content'] = "".join(pa)
        yield item
