from urllib import request,parse
import hashlib
import json
import time,random


def getMD5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value,encoding='utf=8')) #此处要注意类型
    value = md5.hexdigest()
    return value

def fanyi(key):
    ts = int(time.time() * 1000)
    salt = ts + random.randint(0,10)
    bv_value = '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    sign_value = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    bv = getMD5(bv_value)
    sign = getMD5(sign_value)

    base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        "i" : key,
        "from" : "AUTO",
        "to" : "AUTO",
        "smartresult" : "dict",
        "client" : "fanyideskweb",
        "salt" : salt,
        "sign" : sign,
        "ts" : ts,
        "bv" : bv,
        "doctype" : "json",
        "version" : "2.1",
        "keyfrom" : "fanyi.web",
        "action" : "FY_BY_REALTIME",
        "typoResult" : "false"
    }

    data = parse.urlencode(data)

    headers = {
        "Host" : "fanyi.youdao.com",
        "Connection" : "keep-alive",
        "Content-Length" : len(data),
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "Origin" : "http://fanyi.youdao.com",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer" : "http://fanyi.youdao.com/",
        # "Accept-Encoding" : "gzip, deflate", 去掉压缩格式
        "Accept-Language" : "zh-CN,zh;q=0.9",
        "Cookie" : "__guid=204659719.534559504233773600.1548986976042.1416; td_cookie=995979844; OUTFOX_SEARCH_USER_ID=-375749467@10.169.0.83; JSESSIONID=aaajvwmRbw6T6booy0MIw; monitor_count=2; OUTFOX_SEARCH_USER_ID_NCOO=159895261.97988907; ___rl__test__cookies=1548987133381"
    }

    req = request.Request(base_url,data=bytes(data,encoding='utf-8'),headers=headers)
    response = request.urlopen(req)

    data_json = response.read().decode('utf-8')
    # print(data_json)
    # print(type(data_json))
    data = json.loads(data_json)
    res = ''
    for item in data["translateResult"]:
        res += item[0]['tgt']
    print(res)

if __name__ == '__main__':
    while True:
        key = input('输入要翻译的内容：')
        fanyi(key)