def IDcard(index):
    num = 10000
    i = 0
    lists =[]
    basestr = '1101021992081'
    for i in range(0,int(index)):
        newstr = basestr+str(num+i)
        lists.append(newstr)
    # print(lists)
    with open('E:\\个税管理系统\\个税后端客户端\\IDcard.txt','w') as f:
        f.write('\r'.join(lists))
    print("ID 生成完成")


def StaffName(index):
    i = 0
    lists = []
    for i in range(0,index):
        name = '性能'+ str(i)
        lists.append(name)
    with open('E:\\个税管理系统\\个税后端客户端\\StaffName.txt','w') as f:
        f.write("\r".join(lists))
    print("姓名生成完成")

def StaffPhone(index):
    basestr = '158108'
    num = 10000
    i = 0
    lists = []
    for i in range(0,index):
        phone = basestr + str(num+i)
        lists.append(phone)
    with open('E:\\个税管理系统\\个税后端客户端\\StaffPhone.txt','w') as f:
        f.write("\r".join(lists))
    print("电话生成完成")

index = 1000
IDcard(index)
StaffName(index)
StaffPhone(index)