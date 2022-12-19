import tkinter as tk
from tkinter import messagebox
from 管理员.add_type import at

# 添加物品类型界面
class add_type_page:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-管理员版-添加物品类型')
        self.root.geometry('600x400')
        self.page = tk.Frame(self.root)
        self.page.pack()

        # 变量说明
        self.type = tk.StringVar()
        self.p1 = tk.StringVar()
        self.p2 = tk.StringVar()
        self.p3 = tk.StringVar()

        # 变量输入
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='物品(<=5种)固有属性：').grid(row=1, column=1)
        tk.Label(self.page, text='名称、说明、地址、手机、邮箱').grid(row=1, column=2)
        tk.Label(self.page, text='如有附加属性，请填写').grid(row=2, column=1, pady=10)
        tk.Label(self.page, text='(最多3个附加属性)  ；如没有，则不填').grid(row=2, column=2, pady=10)

        tk.Label(self.page, text='物品类型：').grid(row=3, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.type).grid(row=3, column=2)

        tk.Label(self.page, text='附加属性1：').grid(row=4, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.p1).grid(row=4, column=2)

        tk.Label(self.page, text='附加属性2：').grid(row=5, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.p2).grid(row=5, column=2)

        tk.Label(self.page, text='附加属性3：').grid(row=6, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.p3).grid(row=6, column=2)

        tk.Button(self.page, text='添加', command=self.add_type).grid(row=8, column=1, pady=20)
        tk.Button(self.page, text='返回', command=self.back).grid(row=8, column=2,pady=20)

    # 添加物品类型
    def add_type(self):
        type = self.type.get()
        p1 = self.p1.get()
        p2 = self.p2.get()
        p3 = self.p3.get()
        if type:
            flag = at.add_type(type, p1, p2, p3) # 如果添加成功，flag=1
            if flag:
                # 告知用户添加成功
                from 管理员.success_at import success_at
                self.page.destroy()
                success_at(self.root)
            else:
                messagebox.showwarning(title='提示', message='抱歉，类型数量已满(最多5种)')
        else:
            messagebox.showwarning(title='提示', message='抱歉，类型名不能为空')

    # 返回上一级
    def back(self):
        from 管理员.AdminPage import AdminPage
        self.page.destroy()
        AdminPage(self.root)

if __name__ == '__main__':
    root = tk.Tk()
    add_type_page(master=root)
    root.mainloop()