import json


class ShixisengPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('shixiseng.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
