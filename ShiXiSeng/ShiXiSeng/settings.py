# -*- coding: utf-8 -*-
BOT_NAME = 'ShiXiSeng'

SPIDER_MODULES = ['ShiXiSeng.spiders']
NEWSPIDER_MODULE = 'ShiXiSeng.spiders'

# 配置mongodb
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Shixiseng"  # 库名
MONGO_COLL = "info"  # collection

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'ShiXiSeng.middlewares.RotateUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = False  # 不遵循robotstxt规定
COOKIES_ENABLED = False  # 关闭cookies，这样每次抓取数据都可以分配不同的cookies
ITEM_PIPELINES = {
    'ShiXiSeng.pipelines.JsonWriterPipeline': 300,
    'ShiXiSeng.pipelines.ShixisengPipeline': 300,
}
