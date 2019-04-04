# -*- coding: utf-8 -*
from .wx_sdk import wx_get_req,wx_post_req

url = 'http://ai.gw.jdcloud.com/wanxianga17/testai'
params = { 
    'type' : 'json',
    'content' : 'json string',
    'appkey' : 'aef164550413cde170bd5e07d0c22d57',
    'sectetkey':'77f17703b63d14d115ed26d507f5a7fa',
}
response = wx_get_req(url=url,params=params)
print(response.text)