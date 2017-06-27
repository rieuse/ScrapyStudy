# -*- coding: utf-8 -*-

# Scrapy settings for ShiXiSeng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ShiXiSeng'

SPIDER_MODULES = ['ShiXiSeng.spiders']
NEWSPIDER_MODULE = 'ShiXiSeng.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'ShiXiSeng.middlewares.RotateUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'ShiXiSeng.pipelines.JsonWriterPipeline': 300,
    # 'ShiXiSeng.pipelines.ShiXiSengPipeline': 300,
}
