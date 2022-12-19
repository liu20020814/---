import tkinter as tk

# 告知用户删除物品成功
class success_di:
    def __init__(self, master:tk.Tk):
        #页面布局
        self.root = master
        self.root.title('删除物品')
        self.root.geometry('300x130')

        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='删除物品成功！').grid(row=1, column=1, pady=10)

        tk.Button(self.page, text='返回', command=self.back).grid(row=2, column=1)

    #返回上一级
    def back(self):
        from 用户.UserPage import UserPage
        self.page.destroy()
        UserPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    success_di(master=root)
    root.mainloop()