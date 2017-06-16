# -*- coding: utf-8 -*-
import scrapy


class ScrapyximalayaItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
