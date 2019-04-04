import requests
import base64
import os
import json
import threading
from queue import Queue
from JD_OCR.ocr import excel


def getImg(path):
    task_q = Queue()
    for each in os.walk(path):
        # print(each)
        for i in each[2]:
            r_path = path + i
            # print(path)
            task_q.put(r_path)
    return task_q

class OCR(threading.Thread):
    def __init__(self,task_q,lock,type=None):
        super(OCR,self).__init__()
        self.task_q = task_q
        self.lock = lock
        self.type = type

    def run(self):
        host = 'http://10.1.21.106:8000'
        dir_path = ''
        if self.type == '1':
            #存入请求的文件路径
            dir_path = 'scan_pupiao_txt/'
        elif self.type == '2':
            dir_path = 'scan_zhuanpiao_txt/'
        elif self.type == '3':
            dir_path = 'invoiceType_pupiao_txt/'
        elif self.type == '4':
            dir_path = 'invoiceType_zhuanpiao_txt/'

        while not self.task_q.empty():
            self.parse_type_api(host=host, dir_path=dir_path)

    def parse_qr_api(self,host,dir_path):
        # print(url)
        url = host + '/qr_api'
        path = self.task_q.get()
        # print(path,self.params)
        # print(params)
        with self.lock:
            self.request_url(path,url,dir_path)

    def parse_type_api(self,host,dir_path):
        # print(url)
        url = host + '/type_api'
        path = self.task_q.get()
        # print(path,self.params)
        # print(params)
        with self.lock:
            self.request_url(path,url,dir_path)

    #post请求，存储response到txt中
    def request_url(self,path,url,dir_path):
        with open(path, "rb") as f:
            base64_data = base64.b64encode(f.read())
            # print(base64_data)
        params = {
            'picture': base64_data
        }
        response = requests.post(url, data=params)
        res = response.text
        req_time = response.elapsed.total_seconds()
        # print(res)
        jsonData = json.loads(res)
        # print(jsonData)
        try:
            txt_name = path.split('/')[1]
            txt = txt_name.split('.')[0]
            with open((dir_path + txt + '.txt'), 'w+', encoding='utf-8') as f:
                jsonData['response_time'] = str(req_time)
                context = str(jsonData).replace(r"'", r'"')
                f.write(context)
                print('文件%s已生成' % txt)
        except:
            txt = path.split('.')[0]
            with open(('error/' + txt + '.txt'), 'w+', encoding='utf-8') as f:
                f.write(str(jsonData))
                print('异常文件%s' % txt)


if __name__ == '__main__':
    index = input('\n\t\t\t\t请选择发票类型:\n\n[1]普票 [2]专票 [3]发票类型--普票 [4]发票类型--专票:\n')
    path = ''
    excel_path = ''
    type = None
    if index == '1':
        type = '1'
        #图片路径
        path = 'scan_pupiao'
        #excel名称
        excel_path = 'scan_pupiao'
    elif index == '2':
        type = '2'
        path = 'scan_zhuanpiao'
        excel_path = 'scan_zhuanpiao'
    elif index == '3':
        type = '3'
        path = 'scan_pupiao'
        excel_path = 'invoiceType_pupiao'
    elif index == '4':
        type = '4'
        path = 'scan_zhuanpiao'
        excel_path = 'invoiceType_zhuanpiao'

    def run_invoice(path,type):
        task_q = getImg(path + r'/')
        lock = threading.Lock()
        t_list = []

        for i in range(10):
            t = OCR(task_q,lock,type)
            t.start()
            t_list.append(t)

        for t in t_list:
            t.join()

    run_invoice(path,type)

    excel = excel.Excel(excel_path)
    if index == '1' or index == '2':
        excel.run_qr()
    if index == '3' or index == '4':
        excel.run_type()