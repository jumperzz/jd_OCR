import json
import os
from JD_OCR.ocr.insert__excel import demo

class Excel(object):
    def __init__(self,dir_path):
        self.dir_path = dir_path

    #京东OCR识别
    def run(self):
        mainExcel = r'C:\Users\thinkpad\Desktop\analysis_' + self.dir_path + '.xls'
        keywordExcelFile = self.dir_path
        #请求体存储的文件路径
        path = self.dir_path + r'_txt/'
        excelProcess = demo.excelProcess(keywordExcelFile, mainExcel)
        allvaluellist = []
        for each in os.walk(path):
            #第三个中包含所有文件名称
            for file in each[2]:
                with open(path+file,'r',encoding='utf-8') as f:
                    text = f.read()
                    jsonData = json.loads(text)
                    try:
                        result = jsonData['result']
                        valueList = [file,result['buyer_name'],result["buyer_tax_no"],result["code"],result["invoice_amount"],
                                     result["invoice_date"],result["invoice_no"],result["invoice_type"],
                                     result["saler_name"],result["saler_tax_no"],result["tax_amount"],
                                     result["total_amount"],result["verify_code"],jsonData['response_time']
                        ]
                        # valueList = [
                        #     file,result["code"],result["invoice_amount"],result["invoice_date"],result["invoice_no"],
                        #     result["invoice_type"],result["tax_amount"],result["total_amount"],
                        #     result["verify_code"],jsonData['response_time']
                        # ]
                        allvaluellist.append(valueList)
                    except:
                        valueList = [file,str(jsonData)]
                        allvaluellist.append(valueList)
            # print('allvalue',allvaluellist)
            excelProcess.save_Excel(allvaluellist)

    #二维码识别
    def run_qr(self):
        mainExcel = r'C:\Users\thinkpad\Desktop\qr_analysis_' + self.dir_path + '.xls'
        keywordExcelFile = self.dir_path
        path = self.dir_path + r'_txt/'
        excelProcess = demo.excelProcess(keywordExcelFile, mainExcel)
        allvaluellist = []
        for each in os.walk(path):
            for file in each[2]:
                with open(path + file, 'r', encoding='utf-8') as f:
                    text = f.read()
                    jsonData = json.loads(text)
                    try:
                        result = jsonData["invoice"]
                        valueList = [
                            file, result['invoiceType'], result["invoiceCode"], result["invoiceNo"],
                            result["invoiceDate"],result["verifyCode"], result["invoiceAmount"],jsonData["response_time"]
                        ]
                        allvaluellist.append(valueList)
                    except:
                        valueList = [file, str(jsonData)]
                        allvaluellist.append(valueList)
            # print('allvalue',allvaluellist)
            excelProcess.save_qr_Excel(allvaluellist)

    #发票类型识别
    def run_type(self):
        mainExcel = r'C:\Users\thinkpad\Desktop\type_analysis_' + self.dir_path + '.xls'
        keywordExcelFile = self.dir_path
        path = self.dir_path + r'_txt/'
        excelProcess = demo.excelProcess(keywordExcelFile, mainExcel)
        allvaluellist = []
        for each in os.walk(path):
            for file in each[2]:
                with open(path + file, 'r', encoding='utf-8') as f:
                    text = f.read()
                    jsonData = json.loads(text)
                    try:
                        result = jsonData
                        valueList = [file, result['invoiceType'],result["returnCode"],result["response_time"]]
                        allvaluellist.append(valueList)
                    except:
                        valueList = [file, str(jsonData)]
                        allvaluellist.append(valueList)
            # print('allvalue',allvaluellist)
            excelProcess.save_InvoiceType_Excel(allvaluellist)