# -*- coding: utf-8 -*-
import scrapy
import requests
from JobsSpider.jobcollection.jobcollection.items import ProxyFliter
class Spider(scrapy.Spider):

    custom_settings = {
        'ITEM_PIPELINES' : {
            # 'jobcollection.pipelines.ProxyFilterPipeline': 200,
            # 'jobcollection.pipelines.RandomProxyPipeline': 300,

        },
        'RANDOM_UA_TYPE' : "random",
        'SPIDER_MIDDLEWARES' : {
            'jobcollection.middlewares.ProxySpiderMiddleware': 1,
        },
    }

    name = 'ip'
    allowed_domains = []

    def start_requests(self):

        url = 'http://ip.chinaz.com/getip.aspx'

        for i in range(4):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self,response):
        print(response.text)





