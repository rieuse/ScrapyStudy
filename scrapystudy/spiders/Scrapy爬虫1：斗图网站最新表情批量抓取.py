from scrapy.http import Request
from bs4 import BeautifulSoup
import scrapy
from scrapystudy.items import ScrapystudyItem


class ExampleSpider(scrapy.Spider):
    name = "doutu"
    allowed_domains = ["doutula.com","sinaimg.cn"]
    # start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 20)]
    start_urls = ['https://www.doutula.com/photo/list/?page=1']

    def parse(self, response):
        img_url = response.xpath('//*[@id="pic-detail"]/div/div[1]/div[2]/a/img/@data-original')
        name = response.xpath ('//*[@id="pic-detail"]/div/div[1]/div[2]/a/p/text()')
        item = ScrapystudyItem()
        item['img_url'] = img_url
        item['name'] = name
        yield item