import requests
import pymysql
from queue import Queue
import threading

db = pymysql.connect('localhost', 'root', '123456', 'userage')
cursor = db.cursor()

def proxy_find():
    task_q = Queue()
    sql = 'select * from proxy;'
    cursor.execute(sql)
    data = cursor.fetchall()
    for each in data:
        proxy = {}
        proxy['host'] = each[0]
        proxy['port'] = each[1]
        proxy['protocol'] = each[2]
        task_q.put(proxy)

    return task_q


class DB_filter(threading.Thread):
    base_url = 'https://www.baidu.com/s?wd=ip'
    def __init__(self,task_q,lock):
        super(DB_filter,self).__init__()
        self.task_q = task_q
        self.lock = lock

    def run(self):
        while not self.task_q.empty():
            item = self.task_q.get()
            proxy = {
                'http': 'http://' + item['host'] + ':' + str(item['port']),
                'https': 'https://' + item['host'] + ':' + str(item['port'])
            }
            try:
                response = requests.get(url=self.base_url,proxies=proxy,timeout=3)
            except:
                with self.lock:
                    self.DB_del(item)
            else:
                if not 200 <= response.status_code < 300:
                    with self.lock:
                        self.DB_del(item)
                else:
                    print('可用%s %s' % (item['host'], item['port']))

    def DB_del(self,item):
        sql = 'delete from proxy where host =%s'
        cursor.execute(sql,(item['host']))
        db.commit()
        print('删除%s %s' % (item['host'], item['port']))


if __name__ == '__main__':
    task_q = proxy_find()
    print(task_q)
    # lock = threading.Lock()
    # t_list = []
    #
    # for i in range(80):
    #     t = DB_filter(task_q,lock)
    #     t.start()
    #     t_list.append(t)
    #
    # for t in t_list:
    #     t.join()

    cursor.close()
    db.close()