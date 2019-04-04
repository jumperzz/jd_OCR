import sdk,os,re
import json

# url = 'http://ai.gw.jdcloud.com/wanxianga17/testai'
url = 'https://aiapi.jd.com/jdai/ocr_invoice'
params = {
    'type' : 'json',
    'content' : 'json string',
    'appkey' : '794e1b02bbd349358a3a351567b63ba0',
    'secretkey':'11b3025a426f6423307b1db011ccbcde',
}



# response = sdk.wx_get_req(url=url, params=params)
for each in os.walk('pupiao/'):
    path = 'pupiao/'+each[2][0]
    response = sdk.wx_post_req(url=url,params=params,img=path)
    res = response.text
    # print(response.text)
    jsonData = json.loads(res)
    print(jsonData)

