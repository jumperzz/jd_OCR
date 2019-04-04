import json
import re

with open('test','r',encoding='utf-8') as f:
    context = f.read()
    jsonData = json.loads(context)
# print(jsonData)
# print(type(jsonData))
headerTop = []
bodyTop = []

for header in jsonData:
    for each in jsonData[header][0]:
        bodydata = jsonData[header][0][each]
        try:
            bodydata = bodydata[0]
            # print(bodydata)
        except:
            bodydata = bodydata
        else:
            for bodyeach in bodydata:
                # print(bodyeach)
                # print(bodydata[bodyeach])
                try:
                    body = bodydata[bodyeach][0]
                except:
                    body = bodydata[bodyeach]
                    if 'XMMC' in body:
                        bodyTop.append(header +':'+ each +':'+ bodyeach)
                        # print(bodydata[bodyeach])
                else:
                    if 'XMMC' in body:
                        bodyTop.append(header +':'+ each +':'+ bodyeach)
                        # print(bodydata[bodyeach])
print(bodyTop)
