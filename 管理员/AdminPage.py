import tkinter as tk
from 管理员.add_type_page import add_type_page
from 管理员.show_type_Page import show_type_page
from 管理员.change_type_page import change_type_page
from 管理员.check import check

'''管理员的主界面-包含功能：
1.添加类型
2.显示类型
3.修改类型
4.审核注册
5.退出登录'''
class AdminPage:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-管理员版')
        self.root.geometry('300x260')
        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)

        tk.Button(self.page, text='添加类型', command=self.add_type).grid(row=1, column=1, pady=20, padx=30)
        tk.Button(self.page, text='显示类型', command=self.show_type).grid(row=1, column=2, pady=20, padx=30)
        tk.Button(self.page, text='修改类型', command=self.change_type).grid(row=2, column=1, pady=20)
        tk.Button(self.page, text='审核注册', command=self.check_r).grid(row=2, column=2, pady=20)
        tk.Button(self.page, text='退出登录', command=self.back).grid(row=3, column=2, pady=20)

    # 审核注册
    def check_r(self):
        self.page.destroy()
        check(self.root)

    # 添加类型
    def add_type(self):
        self.page.destroy()
        add_type_page(self.root)

    # 显示类型
    def show_type(self):
        self.page.destroy()
        show_type_page(self.root)

    # 修改类型
    def change_type(self):
        self.page.destroy()
        change_type_page(self.root)

    # 返回上一级
    def back(self):
        from 登录.LoginPage import LoginPage
        self.page.destroy()
        LoginPage(self.root)

if __name__ == '__main__':
    root = tk.Tk()
    AdminPage(master=root)
    root.mainloop()