import scrapy


class ShixisengItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    company = scrapy.Field()
    people = scrapy.Field()
    place = scrapy.Field()
    education = scrapy.Field()
    money = scrapy.Field()
    week = scrapy.Field()
    month = scrapy.Field()
    lure = scrapy.Field()
    description = scrapy.Field()
    data = scrapy.Field()
