# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobcollectionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProxyFliter(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    host = scrapy.Field()
    port = scrapy.Field()
    protocol = scrapy.Field()