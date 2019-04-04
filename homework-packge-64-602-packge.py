
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import zipfile
import os
import os.path

class YaSuo:

    bj =False


    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(450, 350)
        self.root.title('万能压缩器')
        self.showlable()
        self.root.mainloop()

    #添加文件

    def press_add(self):
        self.paths = tkinter.filedialog.askopenfilenames(title ='请选择要压缩的文件') #获得需要添加的文件路径
        print(self.paths)
        self.strfile = '\n'.join(self.paths) #将文件路径转换为字符窜并换行输出
        if self.val.set(self.strfile) != '':

            print(self.strfile)

            self.val.set(self.strfile)

            tkinter.messagebox.showinfo('提示', '添加文件成功')
        else:
            self.val.set('文件未添加')

        self.bj = True



    #压缩文件
    def press_ys(self):
        try:
            if self.bj == True:

                if self.val.get() != '':#  判断添加的的文件是否为空


                    # 弹出对话框返回压缩路径
                    self.dirpath = tkinter.filedialog.askdirectory(title = '请选择压缩路径')

                    print(self.dirpath)
                    self.zf = zipfile.ZipFile(self.dirpath + '/压缩.zip','w')  #创建压缩文件
                    #遍历文件信息
                    for i in self.paths:# 便利压缩路径
                        self.zf.write(i,os.path.basename(i)) #压缩文件
                        self.zf.close()

                        #压缩成功后并弹出提示
                        tkinter.messagebox.showinfo('提示','压缩成功,压缩路径' +self.dirpath +'/压缩.zip')
                    else:
                        tkinter.messagebox.showinfo('提示', '请请选择压缩路径')

                else:
                    tkinter.messagebox.showinfo('提示', '请请选择压缩路径')
        except PermissionError:

            tkinter.messagebox.showinfo('提示', '请请选择压缩路径')


    #解压文件

    def press_jy(self):
        try:
            #选择压缩文件
            self.jypath = tkinter.filedialog.askopenfilename(title = '选择解压文件',filetypes = [('zip file','*.zip')])


            result = ''.join(self.jypath)
            result1 = str(result)
            result2 = result1.split('.')
            if result2[-1] == 'zip':

                #压缩路径
                self.zippath = tkinter.filedialog.askdirectory(title = '请选择解压路径')
                self.zf = zipfile.ZipFile(self.jypath,'r') #读出要解压的文件
                self.zf.extractall(self.zippath)  #解压所有文件
                self.zf.close()
                # 弹出提示框
                tkinter.messagebox.showinfo('提示', '解压成功,解压路径:' + self.zippath)

            else:
                tkinter.messagebox.showinfo('提示', '请选择要解压的文件')



        except AttributeError:
            tkinter.messagebox.showinfo('提示', '请选择要解压的文件')

    #显示区域
    def showlable(self):

        def hello(self):
            print('帮助文档')
        # 创建总菜单
        menubar = tkinter.Menu(self.root)
        # 创建一个下拉菜单，并且加入文件菜单
        filemenu = tkinter.Menu(menubar)
        # 创建下来菜单的选项
        filemenu.add_command(label="about", command=hello)
        # 创建下拉菜单的分割线
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # 将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
        menubar.add_cascade(label="File", menu=filemenu)

        # 显示总菜单
        self.root.config(menu=menubar)


        btn_add = tkinter.Button(self.root,text = '添加文件',command = self.press_add).place(x=37.5, y=20,width =100,height = 60)

        btn_ys = tkinter.Button(self.root,text = '压缩文件',command = self.press_ys).place(x=175, y=20,width =100,height = 60)

        btn_jy = tkinter.Button(self.root,text = '解压文件',command =self.press_jy).place(x=312.5, y=20,width =100,height = 60)


        self.val = tkinter.StringVar()
        self.val.set('没有文件信息')

        label1 = tkinter.Label(self.root,textvariable =self.val,bg = 'yellow').place(x=37.5, y=100,width =375,height = 30)

        self.root.mainloop()






yasuo1 =YaSuo()
















