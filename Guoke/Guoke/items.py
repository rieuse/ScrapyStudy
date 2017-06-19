# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuokeItem(scrapy.Item):
    title = scrapy.Field()
    Focus = scrapy.Field()
    answer = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()