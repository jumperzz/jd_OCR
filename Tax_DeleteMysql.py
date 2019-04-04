import pymysql
from tkinter import *

root = Tk()
root.minsize(200,100)

frame_bord = Frame(width=400,height=350,bg='#cccccc')

button_del = Button(frame_bord,text = '删除',width = 5,height =1,command = lambda :main(0)).grid(row = 0,column = 0)
button_clear = Button(frame_bord,text = '更新',width = 5,height =1,command = lambda : main(1)).grid(row = 0,column = 1)

def taxTabel(db,cursor,sql,table_list = [],user_no = ''):
    for table in table_list:
        pre_sql = sql % (table, user_no)
        print(pre_sql)
        cursor.execute(pre_sql)
        db.commit()

def main(use_method_choice):
    try:
        db = pymysql.connect('10.1.1.237','root','ele&DB','pitax_test')
        cursor = db.cursor()
        delPra = {
            'table_list' : [
                "PI_DEDUCTION_EDUCATION_DEGREE", "PI_DEDUCTION_EDUCATION_SKILL",
                "PI_DEDUCTION_EDU_CHILD", "PI_DEDUCTION_ELDER_COMMON",
                "PI_DEDUCTION_ELDER_INFO","PI_DECLARATION_FORM", "PI_DEDUCTION_ELDER_JOINER",
                "PI_DEDUCTION_HOUSING_INFO", "PI_DEDUCTION_HOUSING_LOAN",
                "PI_DEDUCTION_HOUSING_RENT", "PI_DEDUCTION_OTHER"
            ],
            'sql' : 'delete from %s where USER_NO = "%s";'
        }
        updPra = {
            'table_list' : [
                "PI_DEDUCTION_EDUCATION_DEGREE", "PI_DEDUCTION_EDUCATION_SKILL",
                "PI_DEDUCTION_EDU_CHILD","PI_DEDUCTION_ELDER_INFO",
                "PI_DEDUCTION_HOUSING_INFO", "PI_DEDUCTION_HOUSING_LOAN",
                "PI_DEDUCTION_HOUSING_RENT", "PI_DEDUCTION_OTHER"
            ],
            'sql' : 'update %s set period_start = "201901",period_end = NULL where USER_NO = "%s"'
        }

        user_no_list = ['2019013023294104382232f8978c741a3bb2baa55cc622e18']
        sql = ''
        table_list = []

        # 0是删除 1是更新
        use_method = use_method_choice

        if use_method == 0:
            sql = delPra['sql']
            table_list = delPra['table_list']
        elif use_method == 1:
            sql = updPra['sql']
            table_list = updPra['table_list']
        for user_no in user_no_list:
            taxTabel(db=db,cursor=cursor,sql=sql,user_no=user_no,table_list=table_list)
            print("执行成功")
        cursor.close()
        db.close()

    except Exception as error:
        print(error)
        db.rollback()

frame_bord.pack(padx = 10,pady = 10)
root.mainloop()