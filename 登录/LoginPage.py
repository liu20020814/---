import tkinter as tk
from tkinter import messagebox
from 登录.db import db
from 用户.UserPage import UserPage
from 管理员.AdminPage import AdminPage
from 登录.RegisterPage import RegisterPage

'''登录主界面，先输入身份类型（0-管理员，1-用户），然后输入账号、密码，登录系统'''
class LoginPage:
    def __init__(self,master):
        # 页面布局
        self.root = master
        self.root.geometry('300x260')
        self.root.title('物品交换系统-登录页')
        self.page = tk.Frame(self.root)
        self.page.pack()

        # 变量说明
        self.type = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # 变量输入
        tk.Label(self.page).grid(row=0,column=0)

        tk.Label(self.page, text='0-管理员/1-用户：').grid(row=1, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.type).grid(row=1, column=2)

        tk.Label(self.page, text='账号：').grid(row=2, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=2, column=2)

        tk.Label(self.page, text='密码(6位)：').grid(row=3, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.password).grid(row=3, column=2)

        tk.Button(self.page, text='注册', command=self.register).grid(row=4, column=2,pady=10)
        tk.Button(self.page, text='登录', command=self.login).grid(row=5, column=1, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=5, column=2)

    # 注册
    def register(self):
        self.page.destroy()
        RegisterPage(self.root)

    # 登录
    def login(self):
        type = self.type.get()
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(type, name, pwd) # 若登录成功，flag=1；若登录失败，flag=0
        if flag:
            if type =='0': # 管理员登录成功
                self.page.destroy()
                AdminPage(self.root)
            elif type =='1': # 用户登录成功
                self.page.destroy()
                UserPage(self.root)
        else:
            messagebox.showwarning(title='提示', message=message)

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)
    root.mainloop()


