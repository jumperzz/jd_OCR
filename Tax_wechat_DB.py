import pymysql
from tkinter import *

root = Tk()
root.minsize(200,100)

frame_bord = Frame(width=400,height=350,bg='#cccccc')

button_del = Button(frame_bord,text = '删除',width = 5,height =1,command = lambda :main(0)).grid(row = 0,column = 0)
# button_clear = Button(frame_bord,text = '更新',width = 5,height =1,command = lambda : main(1)).grid(row = 0,column = 1)

def taxTabel(db,cursor,sql,table_list = [],uid = ''):
    for table in table_list:
        pre_sql = sql % (table, uid)
        print(pre_sql)
        cursor.execute(pre_sql)
        db.commit()

def main(use_method_choice):
    try:
        db = pymysql.connect('10.1.1.231','root','ele&DB','personal_tax')
        cursor = db.cursor()
        delPra = {
            'table_list' : [
                "tax_deduction_education_degree", "tax_deduction_education_skill", "tax_deduction_edu_child",
                "tax_deduction_elder", "tax_deduction_elder_applicant", "tax_deduction_elder_joiner",
                "tax_deduction_housing_loan", "tax_deduction_housing_rent", "tax_submit_note",
                "tax_deduction_special"
            ],
            'sql' : 'delete from %s where uid = "%s";'
        }

        upPra = {
            'table_list': [],
            'sql' : ''
        }

        uid_list = ['c60edd21-6b51-498e-ab4f-3c102a4a51a4']
        sql = ''
        table_list = []

        # 0是删除 1是更新
        use_method = use_method_choice

        if use_method == 0:
            sql = delPra['sql']
            table_list = delPra['table_list']

        for uid in uid_list:
            taxTabel(db=db,cursor=cursor,sql=sql,uid=uid,table_list=table_list)
            print("执行成功")
        cursor.close()
        db.close()

    except Exception as error:
        print(error)
        db.rollback()

frame_bord.pack(padx = 10,pady = 10)
root.mainloop()