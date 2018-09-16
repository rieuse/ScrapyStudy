# -*- coding: utf-8 -*-
import scrapy


class BaiduWenkuItem(scrapy.Item):
    query = scrapy.Field()
    summary = scrapy.Field()
    introduce = scrapy.Field()
    business_circles = scrapy.Field()
