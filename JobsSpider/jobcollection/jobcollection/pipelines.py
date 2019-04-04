# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import requests

class JobcollectionPipeline(object):
    def process_item(self, item, spider):
        return item

class RandomProxyPipeline(object):
    def process_item(self, items, spider):
        self.db = pymysql.connect('127.0.0.1', 'root', '123456', 'userage')
        self.cursor = self.db.cursor()
        pre_sql = 'insert into proxy(host,port,protocol) VALUES ("%s",%d,"%s") on duplicate KEY UPDATE port = VALUES (port),protocol = VALUES (protocol);'
        sql = pre_sql % (items['host'],int(items['port']),items['protocol'].lower())
        # print(sql)
        try:
            self.cursor.execute(sql)
            print('插入成功')
        except Exception as error:
            print(error)
            self.db.rollback()
        else:
            self.db.commit()

        self.db.close()
        self.cursor.close()
        return items


class ProxyFilterPipeline(object):
    def process_item(self,items, spider):
        # print(items)
        base_url = 'https://www.baidu.com/s?wd=ip'
        proxy = {
            'http': 'http://' + items['host'] + ':' + str(items['port']),
            'https': 'https://' + items['host'] + ':' + str(items['port']),
        }
        try:
            response = requests.get(url=base_url, proxies=proxy, timeout=1)
        except:
            pass
        else:
            if 200 <= response.status_code < 300:
                return items
            else:
                print('连不上')




