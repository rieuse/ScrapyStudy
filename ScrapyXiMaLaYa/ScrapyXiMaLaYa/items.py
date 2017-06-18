# -*- coding: utf-8 -*-
import scrapy


class ScrapyximalayaItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()


class ScrapydetaileItem(scrapy.Item):
    id = scrapy.Field()
    play_path_64 = scrapy.Field()
    # play_path_32 = scrapy.Field()
    # title = scrapy.Field()
    # nickname = scrapy.Field()
    # cover_url = scrapy.Field()
    # formatted_created_at = scrapy.Field()
    # album_title = scrapy.Field()
    # intro = scrapy.Field()
    # category_title = scrapy.Field()
