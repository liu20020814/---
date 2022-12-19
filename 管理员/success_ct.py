import tkinter as tk

# 告知用户修改成功
class success_ct:
    def __init__(self, master:tk.Tk):
        #页面布局
        self.root = master
        self.root.title('修改物品类型')
        self.root.geometry('300x130')

        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='修改物品类型成功！').grid(row=1, column=1, pady=10)

        tk.Button(self.page, text='返回', command=self.back).grid(row=2, column=1)

    # 返回上一级
    def back(self):
        from 管理员.AdminPage import AdminPage
        self.page.destroy()
        AdminPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    success_ct(master=root)
    root.mainloop()