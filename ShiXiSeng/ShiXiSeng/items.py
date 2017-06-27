# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixisengItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    company = scrapy.Field()
    people = scrapy.Field()
    place = scrapy.Field()
    money = scrapy.Field()
    week = scrapy.Field()
    month = scrapy.Field()
    lure = scrapy.Field()
    description = scrapy.Field()
    data = scrapy.Field()
