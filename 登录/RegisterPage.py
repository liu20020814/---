import tkinter as tk
from tkinter import messagebox
from 登录.check_register import cr
from 登录.write_register import wr

# 注册界面
class RegisterPage:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('注册新账号')
        self.root.geometry('400x380')
        self.page = tk.Frame(self.root)
        self.page.pack()

        # 变量说明
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.name = tk.StringVar()
        self.home = tk.StringVar()
        self.phone = tk.StringVar()
        self.email = tk.StringVar()

        # 变量输入
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='账号：').grid(row=1, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)

        tk.Label(self.page, text='密码(6位)：').grid(row=2, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=2)

        tk.Label(self.page, text='姓名：').grid(row=3, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.name).grid(row=3, column=2)

        tk.Label(self.page, text='住址：').grid(row=4, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.home).grid(row=4, column=2)

        tk.Label(self.page, text='手机号：').grid(row=5, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.phone).grid(row=5, column=2)

        tk.Label(self.page, text='邮箱：').grid(row=6, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.email).grid(row=6, column=2)

        tk.Button(self.page, text='注册', command=self.register).grid(row=7, column=1, pady=10)
        tk.Button(self.page, text='返回', command=self.back).grid(row=7, column=2)

    # 注册
    def register(self):
        username = self.username.get()
        pwd = self.password.get()
        name = self.name.get()
        home = self.home.get()
        phone = self.phone.get()
        email = self.email.get()

        flag, message = cr.check_register(username, pwd, name, home, phone, email) # 若注册成功,flag=1
        if flag:
            wr.write_register(username, pwd, name, home, phone, email) # 写入注册
            # 告诉用户注册成功
            from success_rg import  success_rg
            self.page.destroy()
            success_rg(self.root)
        else:
            messagebox.showwarning(title='提示', message=message)

    # 返回上一级
    def back(self):
        from 登录.LoginPage import LoginPage
        self.page.destroy()
        LoginPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    RegisterPage(master=root)
    root.mainloop()