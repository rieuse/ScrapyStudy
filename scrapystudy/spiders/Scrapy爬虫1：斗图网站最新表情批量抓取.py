import scrapy
from scrapystudy.items import DoutuItem
import requests

class doutu(scrapy.Spider):
    name = "doutu"
    allowed_domains = ["doutula.com","sinaimg.cn"]
    # start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 20)]
    start_urls = ['https://www.doutula.com/photo/list/?page=1']

    def parse(self, response):
        # img_url = response.xpath('//*[@id="pic-detail"]/div/div[1]/div[2]/a/img/@data-original')
        # name = response.xpath ('//*[@id="pic-detail"]/div/div[1]/div[2]/a/p/text()')
        i = 0
        for content in response.xpath('//*[@id="pic-detail"]/div/div[1]/div[2]/a'):
            i += 1
            item = DoutuItem()
            item['img_url'] = 'http:' + content.xpath('//img/@data-original').extract()[i]
            item['name'] = content.xpath('//p/text()').extract()[i]
            try:
                r = requests.get(item['img_url'])
                filename = 'doutu\\{}'.format(item['name']) + '.gif'
                with open(filename, 'wb') as fo:
                    fo.write(r.content)
            except:
                print('')
            yield item
