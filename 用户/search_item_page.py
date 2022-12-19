import tkinter as tk
import json
from tkinter import ttk
from tkinter import messagebox

# 所有搜索物品操作的父类
class search_type0:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-用户版-搜索物品')
        self.root.geometry('800x500')
        self.create_page()

        # 变量说明、变量输入
        self.s_name = tk.StringVar()
        self.label = tk.Label(text='物品名称：')
        self.label.pack(anchor=tk.W, pady=20,padx=20)
        self.entry = tk.Entry(textvariable=self.s_name)
        self.entry.pack(anchor=tk.W,padx=20)
        self.bt1 = tk.Button(text='搜索', command=self.show_data_frame)
        self.bt1.pack(anchor=tk.W, padx=130, pady=20)
        self.bt2 = tk.Button(text='返回', command=self.back)
        self.bt2.pack(anchor=tk.E, padx=20, pady=20)

    # 使用treeview搭建展示数据的框架
    def create_page(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        columns = ['name','phone','mail','introduction','email','p1','p2','p3']
        self.tree_view = ttk.Treeview(show='headings', columns=columns)
        self.tree_view.column('name', width=40, anchor='center')
        self.tree_view.column('phone', width=80, anchor='center')
        self.tree_view.column('mail', width=80, anchor='center')
        self.tree_view.column('introduction', width=80, anchor='center')
        self.tree_view.column('email', width=80, anchor='center')
        self.tree_view.column('p1', width=40, anchor='center')
        self.tree_view.column('p2', width=40, anchor='center')
        self.tree_view.column('p3', width=40, anchor='center')

        # 添加滚动条
        self.roll = ttk.Scrollbar(self.root)
        self.roll.pack(side='right', fill='y')
        self.roll.config(command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=self.roll.set)

        # 显示表头
        self.tree_view.heading('name', text='名称')
        self.tree_view.heading('phone', text='手机')
        self.tree_view.heading('mail', text='地址')
        self.tree_view.heading('introduction', text='说明')
        self.tree_view.heading('email', text='邮箱')
        self.headings()

        self.tree_view.pack(fill=tk.BOTH)

    # 返回上一层
    def back(self):
        from 用户.UserPage import UserPage
        self.tree_view.destroy()
        self.bt1.forget()
        self.bt2.forget()
        self.label.forget()
        self.entry.forget()
        self.roll.forget()
        UserPage(self.root)

    # 展示具体数据
    def show_data_frame(self):
        for child in self.tree_view.get_children():
            self.tree_view.delete(child)
        thename = self.s_name.get()
        self.flag = 0 # 物品存在的标志
        self.read()
        for item in self.items:
            if thename == item['name']:
                self.tree_view.insert('',index=+1 ,values=(
                    item['name'],item['phone'],item['mail'],item['introduction'],item['email'],
                    item['p1'],item['p2'],item['p3']
            ))
                self.flag = 1
        if self.flag ==0:
            messagebox.showwarning(title='提示', message='很抱歉，该物品不存在')

    # 读入不同类型物品的特有属性（父类中空实现）
    def headings(self):
        pass

    # 打开对应的json（父类中空实现）
    def read(self):
        pass

# 类型一-json1
class search_type1(search_type0):
    def __init__(self,master:tk.Tk):
        super().__init__(master)

    def headings(self):
        self.tree_view.heading('p1', text=self.types[0]['p1'])
        self.tree_view.heading('p2', text=self.types[0]['p2'])
        self.tree_view.heading('p3', text=self.types[0]['p3'])

    def read(self):
        with open('../物品数据库/1.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.items = json.loads(text)

# 类型二-json2
class search_type2(search_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def headings(self):
        self.tree_view.heading('p1', text=self.types[1]['p1'])
        self.tree_view.heading('p2', text=self.types[1]['p2'])
        self.tree_view.heading('p3', text=self.types[1]['p3'])

    def read(self):
        with open('../物品数据库/2.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.items = json.loads(text)

# 类型三-json3
class search_type3(search_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def headings(self):
        self.tree_view.heading('p1', text=self.types[2]['p1'])
        self.tree_view.heading('p2', text=self.types[2]['p2'])
        self.tree_view.heading('p3', text=self.types[2]['p3'])

    def read(self):
        with open('../物品数据库/3.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.items = json.loads(text)

# 类型四-json4
class search_type4(search_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def headings(self):
        self.tree_view.heading('p1', text=self.types[3]['p1'])
        self.tree_view.heading('p2', text=self.types[3]['p2'])
        self.tree_view.heading('p3', text=self.types[3]['p3'])

    def read(self):
        with open('../物品数据库/4.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.items = json.loads(text)

# 类型五-json5
class search_type5(search_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def headings(self):
        self.tree_view.heading('p1', text=self.types[4]['p1'])
        self.tree_view.heading('p2', text=self.types[4]['p2'])
        self.tree_view.heading('p3', text=self.types[4]['p3'])

    def read(self):
        with open('../物品数据库/5.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.items = json.loads(text)

if __name__ == '__main__':
    root = tk.Tk()
    search_type1(root)
    root.mainloop()
