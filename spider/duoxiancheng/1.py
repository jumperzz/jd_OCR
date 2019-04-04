import pymysql
from urllib import request
import re
import time

class ProxyManager():
    base_url = 'https://www.xicidaili.com/nt/%s'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    def __init__(self):
        self.db = pymysql.connect('127.0.0.1','root','123456','userage')
        self.cursor = self.db.cursor()

    def proxyPrase(self):
        host_list = []
        for i in range(1,5 + 1):
            fullurl = self.base_url % i
            req = request.Request(fullurl,headers=self.headers)
            response = request.urlopen(req)
            time.sleep(0.8)

            html = response.read().decode()
            # print(html)
            com = re.compile(r'<tr(.*?)>(.*?)</tr>',re.S)
            data = com.findall(html)[1:]
            # print(data)
            for each in data:
                # print(each[1])
                # print(type(each[1]))
                com = re.compile('<td>(.*?)</td>')
                data = com.findall(each[1])
                host_list.append(data)
        # return host_list
        print(host_list)

    def saveSpider(self):
        host_list = self.proxyPrase()
        # print(host_list)
        sql = 'insert into proxy(host,port,protocol) VALUES ("%s",%d,"%s") on duplicate KEY update port=VALUES (port),protocol=VALUES (protocol)'
        try:
            for proxy in host_list:
                host = proxy[0]
                port = int(proxy[1])
                protocol = proxy[2]
                # print(host,port,protocl)
                data = sql % (host,port,protocol)
                self.cursor.execute(data)
                self.db.commit()
            self.cursor.close()
            self.db.close()
            print('OK')
        except Exception as error:
            print(error)

if __name__ == '__main__':
    ProxyManager().proxyPrase()