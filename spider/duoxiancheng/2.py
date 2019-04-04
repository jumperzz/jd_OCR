import pymysql
import threading
from queue import Queue
import requests
db = pymysql.connect('127.0.0.1', 'root', '123456', 'userage')
cursor = db.cursor()

def getProxy():
    proxy_q = Queue()
    sql = 'select * from proxy;'
    cursor.execute(sql)
    res = cursor.fetchall()
    for each in res :
        data = {}
        data['host'] = each[0]
        data['port'] = each[1]
        data['protocol'] = each[2]
        proxy_q.put(data)
    # 所有IP加入队列
    return proxy_q

class ProxyFilter(threading.Thread):
    base_url = 'https://www.baidu.com/s?wd=ip'
    def __init__(self,proxy_q,lock):
        super(ProxyFilter, self).__init__()
        self.proxy_q = proxy_q
        self.lock = lock

    def run(self):
        while not self.proxy_q.empty():
            item = self.proxy_q.get()
            # print(item)
            proxy = {
                'http':'http://' + item['host'] + ':' + str(item['port']),
                'https':'http://' + item['host'] + ':' + str(item['port'])
            }
            try:
                response = requests.get(url=self.base_url,proxies=proxy,timeout=3)
                # print(response.status_code)
                print('可用%s %s' % (item['host'],item['port']))
            except Exception as error:
                with self.lock:
                    self.drop_proxy(item)
            else:
                if not 200 <= response.status_code <300:
                    with self.lock:
                        self.drop_proxy(item)

    def drop_proxy(self,item):
        sql = 'delete from proxy where host =%s'
        cursor.execute(sql,(item['host']))
        db.commit()
        print('删除%s %s' % (item['host'], item['port']))

if __name__ == '__main__':
    proxy_q = getProxy()
    lock = threading.Lock()
    t_list = []
    for i in range(50):
        t = ProxyFilter(proxy_q,lock)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    cursor.close()
    db.close()