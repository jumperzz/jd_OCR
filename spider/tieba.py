from urllib import request,parse
import os

base_url = 'https://tieba.baidu.com/f?ie=utf-8'
kw = input('请输入贴吧名称：')
start = input('起始：')
end = input('结束：')


def tieba(kw,start,end):
    #根据输入名称 建立文件夹
    if not os.path.exists(kw):
        os.makedirs(kw)

    #exit()

    qs = {
        'kw': kw,
    }

    for i in range(int(start),int(end) + 1):
        #算出pagenum的值
        pn = (i - 1) * 50
        qs['pn'] = str(pn)
        qs_data = parse.urlencode(qs)

        fullurl = base_url + qs_data
        print('downloading page %s'%fullurl)
        response = request.urlopen(fullurl)
        # print(response.read().decode('UTF-8'))
        with open(kw + '/' + str(i) + '.html','w',encoding='utf-8') as f:
            html = response.read().decode('utf-8')
            f.write(html)

if __name__ == '__main__':
    tieba(kw,start,end)