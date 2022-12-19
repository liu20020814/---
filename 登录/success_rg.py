import tkinter as tk

# 告知用户注册成功
class success_rg:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('注册新账号')
        self.root.geometry('300x130')

        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='注册成功，等待管理员审核...').grid(row=1, column=1)
        tk.Label(self.page, text='审核时间约7个工作日内，请检查短信/邮箱').grid(row=2, column=1, pady=5)

        tk.Button(self.page, text='返回', command=self.back).grid(row=3, column=1)

    # 返回上一级
    def back(self):
        from 登录.LoginPage import LoginPage
        self.page.destroy()
        LoginPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    success_rg(master=root)
    root.mainloop()