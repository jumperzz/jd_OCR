import sdk,os
import json
import threading
from queue import Queue
import excel

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
        url = 'https://aiapi.jd.com/jdai/ocr_invoice'
        dir_path = ''
        if self.type == '1':
            dir_path = 'scan_pupiao_txt/'
        elif self.type == '2':
            dir_path = 'scan_zhuanpiao_txt/'
        elif self.type == '3':
            url = 'https://aiapi.jd.com/jdai/ocr_idcard'
            dir_path = 'IDcard_txt/'
        elif self.type == '4':
            dir_path = 'dianpiao_txt/'

        while not self.task_q.empty():
            self.parse(url=url,dir_path=dir_path)

    def parse(self,url,dir_path):
        params = {
            'type': 'json',
            'content': 'json string',
            'appkey': '794e1b02bbd349358a3a351567b63ba0',
            'secretkey': '11b3025a426f6423307b1db011ccbcde',
        }
        # print(url)
        path = self.task_q.get()
        # print(path,self.params)
        # print(params)
        with self.lock:
            params['timestamp'],params['sign'] = sdk.sign(params['secretkey'])
            params.pop('secretkey')
            response = sdk.wx_post_req(url=url,params=params,img=path)
            res = response.text
            req_time = response.elapsed.total_seconds()
            # print(res)
            jsonData = json.loads(res)
            try:
                jsonData = jsonData['result']
                # print(jsonData)
                txt_name = path.split('/')[1]
                txt = txt_name.split('.')[0]
                with open((dir_path + txt + '.txt'),'w+',encoding='utf-8') as f:
                    jsonData['response_time'] = str(req_time)
                    context = str(jsonData).replace(r"'",r'"')
                    f.write(context)
                    print('文件%s已生成'% txt)
            except:
                txt = path.split('.')[0]
                with open(('error/'  + txt + '.txt'),'w+',encoding='utf-8') as f:
                    f.write(str(jsonData))
                    print('异常文件%s'% txt)

if __name__ == '__main__':
    index = input('\t\t请选择发票类型\n[1]普票 [2]专票 [3]身份证 [4]电票:\n')
    path = ''
    type = None
    if index == '1':
        type = '1'
        path = 'pupiao'
    elif index == '2':
        type = '2'
        path = 'zhuanpiao'
    elif index == '3':
        path = 'IDcard'
        type = '3'
    elif index == '4':
        type = '4'
        path = 'dianpiao'

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

    excel = excel.Excel(path)
    excel.run()