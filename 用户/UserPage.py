import tkinter as tk
from 用户.choose_type import choose_type1,choose_type2,choose_type3,choose_type4,choose_type5

'''用户的主界面-包含功能：
1.添加物品
2.搜索物品
3.查看物品
4.删除物品
5.修改物品
6.退出登录'''
class UserPage:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-用户版')
        self.root.geometry('300x260')
        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)

        tk.Button(self.page, text='添加物品', command=self.choose_types1).grid(row=1, column=1, pady=20,padx=30)
        tk.Button(self.page, text='搜索物品', command=self.choose_types2).grid(row=1, column=2, pady=20,padx=30)
        tk.Button(self.page, text='查看物品', command=self.choose_types3).grid(row=2, column=1, pady=20)
        tk.Button(self.page, text='删除物品', command=self.choose_types4).grid(row=2, column=2, pady=20)
        tk.Button(self.page, text='修改物品', command=self.choose_types5).grid(row=3, column=1, pady=20)
        tk.Button(self.page, text='退出登录', command=self.back).grid(row=3, column=2, pady=20)

    # 添加物品
    def choose_types1(self):
        self.page.destroy()
        choose_type1(self.root)

    # 搜索物品
    def choose_types2(self):
        self.page.destroy()
        choose_type2(self.root)

    # 查看物品
    def choose_types3(self):
        self.page.destroy()
        choose_type3(self.root)

    # 删除物品
    def choose_types4(self):
        self.page.destroy()
        choose_type4(self.root)

    # 修改物品
    def choose_types5(self):
        self.page.destroy()
        choose_type5(self.root)

    # 退出登录
    def back(self):
        self.page.destroy()
        from 登录.LoginPage import LoginPage
        LoginPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    UserPage(master=root)
    root.mainloop()
