import json,pymysql

def getUser():
    try:
        db = pymysql.connect('localhost', 'root', '123456', 'userage')

        cursor = db.cursor()

        sql = "select * from staffer"

        cursor.execute(sql)

        data = cursor.fetchall()

        print(u'原始数据是：', data)

        cursor.close()
        db.close()

        jsondata = []

        for each in data:
            data = {}
            data['id'] = each[0]
            data['name'] = each[1]
            data['de'] = each[2]
            data['to'] = each[3]
            jsondata.append(data)
        print(u"转换为列表字典的数据", jsondata)
    except:
        print(u"数据库异常")
    else:
        jsondatar = json.dumps(jsondata, ensure_ascii=False)
        print(jsondatar)

if __name__ == "__main__":
    getUser()



