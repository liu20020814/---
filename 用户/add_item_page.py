import tkinter as tk
import json
from tkinter import messagebox
from 用户.success_ai import success_ai

#所有添加物品操作的父类
class add_type:
    def __init__(self, master:tk.Tk):
        #页面布局
        self.root = master
        self.root.title('物品交换系统-用户版-添加物品')
        self.root.geometry('600x400')

        #变量说明
        self.name = tk.StringVar()
        self.introduction = tk.StringVar()
        self.mail = tk.StringVar()
        self.phone = tk.StringVar()
        self.email = tk.StringVar()
        self.p1 = tk.StringVar()
        self.p2 = tk.StringVar()
        self.p3 = tk.StringVar()

        self.page = tk.Frame(self.root)
        self.page.pack()

        #变量输入
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='  *名称：').grid(row=1, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.name).grid(row=1, column=2, pady=10,padx=5)

        tk.Label(self.page, text='  *手机：').grid(row=1, column=3, pady=10)
        tk.Entry(self.page, textvariable=self.phone).grid(row=1, column=4, pady=10,padx=5)

        tk.Label(self.page, text='  地址：').grid(row=2, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.mail).grid(row=2, column=2, pady=10,padx=5)

        tk.Label(self.page, text='  说明：').grid(row=2, column=3, pady=10)
        tk.Entry(self.page, textvariable=self.introduction).grid(row=2, column=4, pady=10,padx=5)

        tk.Label(self.page, text='  邮箱：').grid(row=3, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.email).grid(row=3, column=2)

        self.show_type()
        tk.Button(self.page, text='添加', command=self.add).grid(row=5, column=2,pady=100)
        tk.Button(self.page, text='返回', command=self.back).grid(row=5,column=4,pady=50)

    #打开对应json（父类中空实现）
    def read(self):
        pass

    #写入对应json（父类中空实现）
    def write(self, json_content):
        pass

    #添加物品操作
    def add(self):
        if self.name.get() and self.phone.get():
            json_content = []
            with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
                text = f.read()
            self.types = json.loads(text)
            self.read()
            #读入json中原有数据
            for c in self.contents:
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
            #添加新数据
            object = {}
            object['name'] = self.name.get()
            object['phone'] = self.phone.get()
            object['mail'] = self.mail.get()
            object['introduction'] = self.introduction.get()
            object['email'] = self.email.get()
            object['p1'] = self.p1.get()
            object['p2'] = self.p2.get()
            object['p3'] = self.p3.get()
            json_content.append(object)
            self.write(json_content)
            self.page.destroy()
            success_ai(self.root)
        else:
            messagebox.showwarning(title='提示', message='很抱歉，*必填项不能输入为空')

    #展示对应属性（父类中空实现）
    def show_type(self):
        pass

    #返回上一层
    def back(self):
        from 用户.UserPage import UserPage
        self.page.destroy()
        UserPage(self.root)

#类型一-json1
class add_type1(add_type):
    def __init__(self,master:tk.Tk):
        super().__init__(master)

    def show_type(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        if self.types[0]['p1']:
            tk.Label(self.page, text=self.types[0]['p1']+':').grid(row=3, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p1).grid(row=3, column=4,padx=10)
        if self.types[0]['p2']:
            tk.Label(self.page, text=self.types[0]['p2']+':').grid(row=4, column=1, pady=10)
            tk.Entry(self.page, textvariable=self.p2).grid(row=4, column=2,padx=10)
        if self.types[0]['p3']:
            tk.Label(self.page, text=self.types[0]['p3']+':').grid(row=4, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p3).grid(row=4, column=4,padx=10)

    def read(self):
        with open('../物品数据库/1.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/1.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

#类型二-json2
class add_type2(add_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def show_type(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        if self.types[1]['p1']:
            tk.Label(self.page, text=self.types[1]['p1']+':').grid(row=3, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p1).grid(row=3, column=4,padx=10)
        if self.types[1]['p2']:
            tk.Label(self.page, text=self.types[1]['p2']+':').grid(row=4, column=1, pady=10)
            tk.Entry(self.page, textvariable=self.p2).grid(row=4, column=2,padx=10)
        if self.types[1]['p3']:
            tk.Label(self.page, text=self.types[1]['p3']+':').grid(row=4, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p3).grid(row=4, column=4,padx=10)

    def read(self):
        with open('../物品数据库/2.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/2.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

#类型三-json3
class add_type3(add_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def show_type(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        if self.types[2]['p1']:
            tk.Label(self.page, text=self.types[2]['p1']+':').grid(row=3, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p1).grid(row=3, column=4,padx=10)
        if self.types[2]['p2']:
            tk.Label(self.page, text=self.types[2]['p2']+':').grid(row=4, column=1, pady=10)
            tk.Entry(self.page, textvariable=self.p2).grid(row=4, column=2,padx=10)
        if self.types[2]['p3']:
            tk.Label(self.page, text=self.types[2]['p3']+':').grid(row=4, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p3).grid(row=4, column=4,padx=10)

    def read(self):
        with open('../物品数据库/3.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/3.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

#类型四-json4
class add_type4(add_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def show_type(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        if self.types[3]['p1']:
            tk.Label(self.page, text=self.types[3]['p1']+':').grid(row=3, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p1).grid(row=3, column=4,padx=10)
        if self.types[3]['p2']:
            tk.Label(self.page, text=self.types[3]['p2']+':').grid(row=4, column=1, pady=10)
            tk.Entry(self.page, textvariable=self.p2).grid(row=4, column=2,padx=10)
        if self.types[3]['p3']:
            tk.Label(self.page, text=self.types[3]['p3']+':').grid(row=4, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p3).grid(row=4, column=4,padx=10)

    def read(self):
        with open('../物品数据库/4.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/4.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

#类型五-json5
class add_type5(add_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def show_type(self):
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.types = json.loads(text)
        if self.types[4]['p1']:
            tk.Label(self.page, text=self.types[4]['p1']+':').grid(row=3, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p1).grid(row=3, column=4,padx=10)
        if self.types[4]['p2']:
            tk.Label(self.page, text=self.types[4]['p2']+':').grid(row=4, column=1, pady=10)
            tk.Entry(self.page, textvariable=self.p2).grid(row=4, column=2,padx=10)
        if self.types[4]['p3']:
            tk.Label(self.page, text=self.types[4]['p3']+':').grid(row=4, column=3, pady=10)
            tk.Entry(self.page, textvariable=self.p3).grid(row=4, column=4,padx=10)

    def read(self):
        with open('../物品数据库/5.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/5.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

if __name__ == '__main__':
    root = tk.Tk()