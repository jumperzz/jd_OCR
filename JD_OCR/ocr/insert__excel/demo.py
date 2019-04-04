# coding=utf-8
import xlwt

class excelProcess(object):
    def __init__(self,keywordExcelFile,mainExcelFile):
        self.keywordExcelFile = keywordExcelFile
        self.mainExcelFile = mainExcelFile

    #将值逐行逐列插入excel
    def WriteSheetRow(self,sheet, rowValueList, rowIndex, isBold):
        i = 0
        style = xlwt.easyxf('font: bold 1')
        # style = xlwt.easyxf('font: bold 0, color red;')#红色字体
        # style2 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold on;') # 设置Excel单元格的背景色为黄色，字体为粗体
        for svalue in rowValueList:
            if isBold:
                sheet.write(rowIndex, i, svalue, style)
            else:
                sheet.write(rowIndex, i, svalue)
            i = i + 1

    #京东OCR
    def save_Excel(self,allvalueList):
        print('作用的表格是：%s'% self.mainExcelFile)
        wbk = xlwt.Workbook(self.mainExcelFile)
        sheet = wbk.add_sheet(self.keywordExcelFile, cell_overwrite_ok=True)

        headList = ["文件名", "buyer_name", "buyer_tax_no", "code", "invoice_amount", "invoice_date",
                    "invoice_no", "invoice_type", "saler_name", "saler_tax_no", "tax_amount", "total_amount",
                    "verify_code", "响应时间"]

        # headList = ["文件名","发票代码", "金额", "开票日期",
        #             "发票号码", "发票类型", "税额", "价税合计",
        #             "校验码", "响应时间"]
        rowIndex = 0
        self.WriteSheetRow(sheet, headList, rowIndex, True)
        print('第1行，表头插入完成')

        for valueList in allvalueList:
            rowIndex = rowIndex + 1
            self.WriteSheetRow(sheet, valueList, rowIndex, False)
            print('第%d行插入完成'%(rowIndex+1))

        wbk.save(self.mainExcelFile)
        print('文件保存完成')

    #二维码识别
    def save_qr_Excel(self,allvalueList):
        print('作用的表格是：%s'% self.mainExcelFile)
        wbk = xlwt.Workbook(self.mainExcelFile)
        sheet = wbk.add_sheet(self.keywordExcelFile, cell_overwrite_ok=True)

        headList = ["文件名",'invoiceType',"invoiceCode","invoiceNo","invoiceDate","verifyCode","invoiceAmount", "响应时间"]
        rowIndex = 0
        self.WriteSheetRow(sheet, headList, rowIndex, True)
        print('第1行，表头插入完成')

        for valueList in allvalueList:
            rowIndex = rowIndex + 1
            self.WriteSheetRow(sheet, valueList, rowIndex, False)
            print('第%d行插入完成'%(rowIndex+1))

        wbk.save(self.mainExcelFile)
        print('文件保存完成')

    #发票类型识别
    def save_InvoiceType_Excel(self,allvalueList):
        print('作用的表格是：%s'% self.mainExcelFile)
        wbk = xlwt.Workbook(self.mainExcelFile)
        sheet = wbk.add_sheet(self.keywordExcelFile, cell_overwrite_ok=True)

        headList = ["文件名", "invoice_type","returnCode","响应时间"]
        rowIndex = 0
        self.WriteSheetRow(sheet, headList, rowIndex, True)
        print('第1行，表头插入完成')

        for valueList in allvalueList:
            rowIndex = rowIndex + 1
            self.WriteSheetRow(sheet, valueList, rowIndex, False)
            print('第%d行插入完成'%(rowIndex+1))

        wbk.save(self.mainExcelFile)
        print('文件保存完成')