# -*- coding: utf-8 -*-
import scrapy
from Guoke.items import GuokeItem


class GuokeSpider(scrapy.Spider):
    name = "guoke"
    allowed_domains = ["guokr.com"]
    start_urls = ['http://www.guokr.com/ask/hottest/?page={}'.format(n) for n in range(1, 2)]
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