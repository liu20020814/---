import tkinter as tk
from tkinter import ttk
import json

# 展示物品类型界面
class show_type_page:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-管理员版-查看物品类型')
        self.root.geometry('600x400')
        self.create_page()

        self.bt = tk.Button(text='返回', command=self.back)
        self.bt.pack(anchor=tk.E, padx=20, pady=20)

    def create_page(self):
        # 使用treeview搭建展示数据的框架
        columns = ['type', 'p1', 'p2', 'p3']
        self.tree_view = ttk.Treeview(show='headings', columns=columns)
        self.tree_view.column('type', width=80, anchor='center')
        self.tree_view.column('p1', width=80, anchor='center')
        self.tree_view.column('p2', width=80, anchor='center')
        self.tree_view.column('p3', width=80, anchor='center')
        self.tree_view.heading('type', text='物品类型')
        self.tree_view.heading('p1', text='附加属性1')
        self.tree_view.heading('p2', text='附加属性2')
        self.tree_view.heading('p3', text='附加属性3')

        # 添加滚动条
        self.roll = ttk.Scrollbar(self.root)
        self.roll.pack(side='right',fill='y')
        self.roll.config(command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=self.roll.set)

        self.tree_view.pack(fill=tk.BOTH)
        self.show_data_frame()


    # 返回上一级
    def back(self):
        from 管理员.AdminPage import AdminPage
        self.tree_view.destroy()
        self.bt.forget()
        self.roll.forget()
        AdminPage(self.root)

    # 展示具体数据
    def show_data_frame(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        for tp in self.types:
            self.tree_view.insert('',index=+1 ,values=(
                tp['type'],tp['p1'],tp['p2'],tp['p3'],
            ))

if __name__ == '__main__':
    root = tk.Tk()
    show_type_page(master=root)
    root.mainloop()