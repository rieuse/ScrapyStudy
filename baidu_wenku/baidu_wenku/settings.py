# -*- coding: utf-8 -*-

BOT_NAME = 'baidu_wenku'

SPIDER_MODULES = ['baidu_wenku.spiders']
NEWSPIDER_MODULE = 'baidu_wenku.spiders'

ROBOTSTXT_OBEY = False
LOG_LEVEL = "INFO"


DOWNLOADER_MIDDLEWARES = {
   'baidu_wenku.middlewares.BaiduWenkuDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {
   'baidu_wenku.pipelines.JsonWriterPipeline': 300,
}

DEFAULT_REQUEST_HEADERS = {
    # 'Cookie' : 'xq_a_token=584d0cf8d5a5a9809761f2244d8d272bac729ed4',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Connection': 'Keep-Alive',
    'referer': 'https://wapbaike.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
}
