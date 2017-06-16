# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyXiMaLaYa project

BOT_NAME = 'ScrapyXiMaLaYa'

SPIDER_MODULES = ['ScrapyXiMaLaYa.spiders']
NEWSPIDER_MODULE = 'ScrapyXiMaLaYa.spiders'

# 配置mongodb
ITEM_PIPELINES = {'ScrapyXiMaLaYa.pipelines.ScrapyximalayaPipeline': 300, }
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "XiMaLaYa"  # 库名
MONGO_COLL = "scrapy_info"  # collection名

# 下面设置随机User Agent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'ScrapyXiMaLaYa.middlewares.RotateUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = False  # 不遵循网站的robots.txt策略
CONCURRENT_REQUESTS = 16  # Scrapy downloader 并发请求(concurrent requests)的最大值
DOWNLOAD_DELAY = 0.5  # 下载同一个网站页面前等待的时间，可以用来限制爬取速度减轻服务器压力。
COOKIES_ENABLED = False  # 关闭cookies
