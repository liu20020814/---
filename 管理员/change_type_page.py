import tkinter as tk
from tkinter import messagebox
from 管理员.change_type import ct

# 修改物品类型界面
class change_type_page:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-管理员版-修改物品类型')
        self.root.geometry('600x400')
        self.page = tk.Frame(self.root)
        self.page.pack()

        # 变量说明
        self.type1 = tk.StringVar()
        self.type2 = tk.StringVar()

        # 变量输入
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='修改前的类型名：').grid(row=1, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.type1).grid(row=1, column=2)

        tk.Label(self.page, text='修改后的类型名：').grid(row=2, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.type2).grid(row=2, column=2)

        tk.Button(self.page, text='修改', command=self.change).grid(row=3, column=1, pady=50)
        tk.Button(self.page, text='返回', command=self.back).grid(row=3, column=2,pady=50)

    # 修改物品类型
    def change(self):
        type1 = self.type1.get()
        type2 = self.type2.get()
        if type1 and type2:
            flag,message = ct.change_type(type1, type2) # 若修改成功，flag=1
            if flag:
                # 告知用户修改成功
                from 管理员.success_ct import success_ct
                self.page.destroy()
                success_ct(self.root)
            else:
                messagebox.showwarning(title='提示', message=message)
        else:
            messagebox.showwarning(title='提示', message='抱歉，类型名不能为空')

    # 返回上一级
    def back(self):
        from 管理员.AdminPage import AdminPage
        self.page.destroy()
        AdminPage(self.root)

if __name__ == '__main__':
    root = tk.Tk()
    change_type_page(master=root)
    root.mainloop()