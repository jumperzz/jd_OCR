import cgi,cgitb,time,pymysql
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers


#print(123)
fs = cgi.FieldStorage()
inputs = {}
for key in fs.keys():
     inputs[key] = fs[key].value

time.sleep(3)

# print(inputs)
# sql = '''insert into staffer values (null,'{}',{},{})'''.format(inputs['user'],inputs['department_id'],inputs['position_id'])
#
# print(sql)
db = pymysql.connect('localhost','root','123456','userage')
cursor = db.cursor()

sql = '''insert into staffer values (null,'{}',{},{})'''.format(inputs['user'],inputs['department_id'],inputs['position_id'])
# print(inputs['user'],inputs['department_id'],inputs['position_id'])
cursor.execute(sql)
db.commit()

time.sleep(3)

sql = '''select * from staffer'''
cursor.execute(sql)

data = cursor.fetchall()

cursor.close()
db.close()



