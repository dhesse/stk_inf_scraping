# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class SplitDateTemperature(object):
    def process_item(self, item, spider):
        """Split the text of the yielded itmes."""
        item['date'], item['temp'] = item['item'].split()
        return item

class ProcessTemp(object):
    def process_item(self, item, spider):
        """Remove degree symbol, cast to int."""
        item['temp'] = int(item['temp'].replace(u'\xb0', ''))
        return item

class ProcessDate(object):
    def process_item(self, item, spider):
        """Remove colon."""
        item['date'] = item['date'].replace(':', '')
        return item
