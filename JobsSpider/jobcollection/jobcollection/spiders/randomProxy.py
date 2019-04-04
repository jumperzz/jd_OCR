# -*- coding: utf-8 -*-
import scrapy
from ..items import ProxyFliter
from scrapy_redis.spiders import RedisSpider
class RandomproxySpider(RedisSpider):
    name = 'randomProxy'
    allowed_domains = ['xicidaili.com']
    # start_urls = ['https://www.xicidaili.com/']
    custom_settings = {
        # 'ITEM_PIPELINES' : {
        #     # 'jobcollection.pipelines.ProxyFilterPipeline': 300,
        #     # 'jobcollection.pipelines.RandomProxyPipeline': 400,
        # },
        'RANDOM_UA_TYPE' : "random",
        'SPIDER_MIDDLEWARES' : {
            'jobcollection.middlewares.RandomHeaderSpiderMiddleware': 1,
        },
    }

    def parse(self, response):
        self.base_url = 'https://www.xicidaili.com/nn/%s'
        # print(response.text)
        for page  in range(1,3):
            fullurl = self.base_url % page
            # print(response.headers)
            yield scrapy.Request(url=fullurl,callback=self.parse_detail)

    def parse_detail(self,response):
        # print(response.headers)
        # items = []
        print(response.url)
        for tr in response.xpath('//table//tr')[1:]:
            item = ProxyFliter()
            td_data = tr.xpath('./td/text()')
            # print(td_data)
            item['host'] = td_data[0].extract()
            item['port'] = td_data[1].extract()
            item['protocol'] = td_data[5].extract()
            # items.append(item)
            yield item
        # return items

