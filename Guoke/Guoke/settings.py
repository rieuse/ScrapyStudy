# -*- coding: utf-8 -*-
BOT_NAME = 'Guoke'
SPIDER_MODULES = ['Guoke.spiders']
NEWSPIDER_MODULE = 'Guoke.spiders'

# 配置mongodb
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Guoke"  # 库名
MONGO_COLL = "Guoke_info"  # collection

# pipeline文件的入口,这里进
ITEM_PIPELINES = {
    'Guoke.pipelines.JsonWriterPipeline': 300,
    'Guoke.pipelines.GuokePipeline': 300,
 }


# 设置随机User_Agent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'Guoke.middlewares.RotateUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = False  # 不遵循网站的robots.txt策略
DOWNLOAD_DELAY = 1  # 下载同一个网站页面前等待的时间，可以用来限制爬取速度减轻服务器压力。
COOKIES_ENABLED = False  # 关闭cookies
