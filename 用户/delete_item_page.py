import tkinter as tk
import json
from tkinter import messagebox
from 用户.success_di import success_di

# 所有删除物品操作的父类
class delete_type:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-用户版-删除物品')
        self.root.geometry('600x400')
        self.page = tk.Frame(self.root)
        self.page.pack()

        # 变量说明
        self.name = tk.StringVar()
        self.phone = tk.StringVar()

        # 变量输入
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='名称：').grid(row=1, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.name).grid(row=1, column=2, pady=10,padx=5)

        tk.Label(self.page, text='手机：').grid(row=2, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.phone).grid(row=2, column=2, pady=10,padx=5)

        tk.Button(self.page, text='删除', command=self.delete).grid(row=5, column=1,pady=100)
        tk.Button(self.page, text='返回', command=self.back).grid(row=5,column=2,pady=50)

    # 打开对应json（父类中空实现）
    def read(self):
        pass

    # 写入对应json（父类中空实现）
    def write(self, json_content):
        pass

    # 删除物品
    def delete(self):
        if self.name.get() and self.phone.get():
            flag = 0
            json_content = []
            with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
                text = f.read()
            self.types = json.loads(text)
            self.read()
            # 除了被删除的物品，将其他所有物品复制回json
            for c in self.contents:
                if c['name'] == self.name.get() and c['phone'] == self.phone.get():
                    flag = 1
                    pass
                else:
                    ob = {}
                    ob['name'] = c['name']
                    ob['phone'] = c['phone']
                    ob['mail'] = c['mail']
                    ob['introduction'] = c['introduction']
                    ob['email'] = c['email']
                    ob['p1'] = c['p1']
                    ob['p2'] = c['p2']
                    ob['p3'] = c['p3']
                    json_content.append(ob)
            if flag :
                self.write(json_content)
                self.page.destroy()
                success_di(self.root)
            else:
                messagebox.showwarning(title='提示', message='很抱歉，物品不存在，请检查名称与手机号是否都正确')
        else:
            messagebox.showwarning(title='提示', message='很抱歉，输入不能为空')

    # 返回上一级
    def back(self):
        from 用户.UserPage import UserPage
        self.page.destroy()
        UserPage(self.root)

# 类型一-json1
class delete_type1(delete_type):
    def __init__(self,master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/1.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/1.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

# 类型二-json2
class delete_type2(delete_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/2.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/2.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

# 类型三-json3
class delete_type3(delete_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/3.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/3.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

# 类型四-json4
class delete_type4(delete_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/4.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/4.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

# 类型五-json5
class delete_type5(delete_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/5.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/5.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

if __name__ == '__main__':
    root = tk.Tk()
    delete_type1(master=root)
    root.mainloop()
