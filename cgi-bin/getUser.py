import cgi,cgitb,pymysql
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers



db = pymysql.connect('localhost','root','123456','userage')
cursor = db.cursor()

sql='''select * from staffer'''

cursor.execute(sql)
data = cursor.fetchall()
cursor.close()
db.close()
html = '''
    <table>
        <tr>
            <td>编号</td>
            <td>姓名</td>
            <td>公寓</td>
            <td>住址</td>
        </tr>'''
html2 ='''
    </table>
'''
for i in range(1):
    print(html)
    for each in data:
        tlc = '''
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%d</td>
                <td>%d</td>
            </tr>
        '''%(each[0],each[1],each[2],each[3])
        print(tlc)
    print(html2)
