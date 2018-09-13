# -*- coding: utf-8 -*-


BOT_NAME = 'cs_com'

SPIDER_MODULES = ['cs_com.spiders']
NEWSPIDER_MODULE = 'cs_com.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
LOG_LEVEL = "INFO"


ITEM_PIPELINES = {
   'cs_com.pipelines.JsonWriterPipeline': 300,
}
DOWNLOADER_MIDDLEWARES = {
   'cs_com.middlewares.RotateUserAgentMiddleware': 543,
}

DEFAULT_REQUEST_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.cs.com.cn/',
            'Cookie': 'wdcid=4f7ab58c02440ae1; wdlast=1531810276',
            'Connection': 'keep-alive',
            'Cache - Control': 'max - age = 0',
        }

cs_com_start_urls = [
    # 要闻
    'http://www.cs.com.cn/xwzx/hg/index.shtml',
    'http://www.cs.com.cn/xwzx/msxf/index.shtml',
    'http://www.cs.com.cn/xwzx/jr/index.shtml',
    'http://www.cs.com.cn/xwzx/hwxx/index.shtml',
    'http://www.cs.com.cn/xwzx/zt2017/index.shtml',
    'http://www.cs.com.cn/xwzx/tzzjy/index.shtml',
    # 公司
    'http://www.cs.com.cn/ssgs/gssd/index.shtml',
    'http://www.cs.com.cn/ssgs/ggjd/index.shtml',
    'http://www.cs.com.cn/ssgs/gsxw/index.shtml',
    'http://www.cs.com.cn/ssgs/ssb/index.shtml',
    'http://www.cs.com.cn/ssgs/zt2017/index.shtml',
    'http://www.cs.com.cn/ssgs/gsxl/index.shtml',
    # 市场
    'http://www.cs.com.cn/gppd/gsyj/index.shtml',
    'http://www.cs.com.cn/gppd/hyyj/index.shtml',
    'http://www.cs.com.cn/gppd/tzpj/index.shtml',
    'http://www.cs.com.cn/gppd/sjjj/index.shtml',
    'http://www.cs.com.cn/gppd/tzzx/index.shtml',
    'http://www.cs.com.cn/gppd/zqxw/index.shtml',
    'http://www.cs.com.cn/gppd/jp/index.shtml',
    'http://www.cs.com.cn/gppd/zt2017/index.shtml',
    'http://www.cs.com.cn/gppd/cb/index.shtml',
    # 新股
    'http://www.cs.com.cn/xg/wysg/index.shtml',
    'http://www.cs.com.cn/xg/03/index.shtml',
    # 基金
    'http://www.cs.com.cn/tzjj/jjdt/index.shtml',
    'http://www.cs.com.cn/tzjj/jjks/index.shtml',
    'http://www.cs.com.cn/tzjj/jjcs/index.shtml',
    'http://www.cs.com.cn/tzjj/smjj/index.shtml',
    'http://www.cs.com.cn/tzjj/tjdh/index.shtml',
    'http://www.cs.com.cn/tzjj/zt2017/index.shtml',
    # 产经
    'http://www.cs.com.cn/cj/hyzx/index.shtml',
    'http://www.cs.com.cn/cj/fcgs/index.shtml',
    'http://www.cs.com.cn/cj/03/index.shtml',
    'http://www.cs.com.cn/cj/zt/index.shtml',
    # 期货
    'http://www.cs.com.cn/zzqh/spqh/index.shtml',
    'http://www.cs.com.cn/zzqh/ysp/index.shtml',
    'http://www.cs.com.cn/zzqh/06/index.shtml',
    'http://www.cs.com.cn/zzqh/qhzk/index.shtml',
    # 债券
    'http://www.cs.com.cn/jg/03/index.shtml',
    'http://www.cs.com.cn/jg/04/index.shtml',
    'http://www.cs.com.cn/jg/05/index.shtml',
    'http://www.cs.com.cn/jg/06/index.shtml',
    'http://www.cs.com.cn/jg/07/index.shtml',
    'http://www.cs.com.cn/jg/08/index.shtml',
    'http://www.cs.com.cn/jg/09/index.shtml',
    'http://www.cs.com.cn/jg/10/index.shtml',
    # 港股
    'http://www.cs.com.cn/gg/ggyw/index.shtml',
    'http://www.cs.com.cn/gg/scpl/index.shtml',
    'http://www.cs.com.cn/gg/gsxw/index.shtml',
    'http://www.cs.com.cn/gg/tzpj/index.shtml',
    'http://www.cs.com.cn/gg/zt2017/index.shtml',
    ]