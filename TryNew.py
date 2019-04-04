import tkinter
root = tkinter.Tk()
root.minsize(300,300)
root.title('菜单测试')

menu = tkinter.Menu(root,tearoff = False)

Open = tkinter.Menu(menu,tearoff = False)
menu.add_cascade(label= 'Open',menu = Open)
Open.add_command(label = 'One')
Open.add_command(label ='two')
Open.add_separator()

Next = tkinter.Menu(Open,tearoff = False)
Open.add_cascade(label = 'Next',menu = Next)
Next.add_command(label ='Three')

root.config(menu = menu)

root.mainloop()