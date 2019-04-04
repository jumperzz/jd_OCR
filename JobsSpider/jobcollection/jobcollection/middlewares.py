# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals,crawler
from fake_useragent import UserAgent
import random



class RandomHeaderSpiderMiddleware(object):
    def __init__(self,crawler):
        super(RandomHeaderSpiderMiddleware,self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self, request,spider):

        def get_ua():
            return getattr(self.ua, self.ua_type)  # 获取ua的ua_type属性，也就是获得random

        request.headers.setdefault('User-Agent', get_ua())



class ProxySpiderMiddleware(object):
    def __init__(self,ip):
        self.ip = ip

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.get('PROXIES'))

    def process_request(self,request,spider):
        ip = random.choice(self.ip)
        request.meta['proxy'] = ip