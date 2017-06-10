# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os


class ScrapystudyPipeline(object):
    # img_url = None
    # name = None
    def process_item(self, item, spider):
        u = 'https://ws1.sinaimg.cn/large/9150e4e5ly1fg5ikjtsdej20hs0hsdk5.jpg'
        img_url = item['img_url']
        name = item['name']
        if not os.path.exists('doutu'):
            print('创建文件夹...')
            os.makedirs('doutu')
        for img, na in zip(img_url, name):
            print(img)
            print(na)
            r = requests.get('https:' + str(img))
            filename = 'doutu\\{}'.format(na) + '.gif'
            with open(filename, 'wb') as fo:
                fo.write(r.content)
                fo.close()
        return print(type(name))



        # def download_img(img_url, name):
        #     if not os.path.exists('doutu'):
        #         print('创建文件夹...')
        #         os.makedirs('doutu')
        #     r = requests.get(img_url)
        #     filename = 'doutu\\{}'.format(name) + '.gif'
        #     with open(filename, 'wb') as fo:
        #         fo.write(r.content)
