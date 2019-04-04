# -*- coding: utf-8 -*-
import scrapy
import requests

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhilian.com']
    start_urls = ['http://zhilian.com/']

    def parse(self, response):
        pass
