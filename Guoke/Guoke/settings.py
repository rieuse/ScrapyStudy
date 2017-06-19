# -*- coding: utf-8 -*-

# Scrapy settings for Guoke project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Guoke'

SPIDER_MODULES = ['Guoke.spiders']
NEWSPIDER_MODULE = 'Guoke.spiders'

# pipeline文件的入口
ITEM_PIPELINES = {
    'Guoke.pipelines.JsonWriterPipeline': 300,
 }
# LOG_LEVEL = 'INFO'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'Guoke.middlewares.RotateUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = False
