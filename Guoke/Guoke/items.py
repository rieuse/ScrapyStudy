# -*- coding: utf-8 -*-
import scrapy


class GuokeItem(scrapy.Item):
    title = scrapy.Field()
    Focus = scrapy.Field()
    answer = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()


class Ggitem(scrapy.Item):
    title = scrapy.Field()
    Focus = scrapy.Field()
    answer = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
