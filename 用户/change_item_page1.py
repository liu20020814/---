import tkinter as tk
import json
from tkinter import messagebox
from 用户.change_item_page2 import change2_type1,change2_type2,change2_type3,change2_type4,change2_type5

# 所有更改物品操作的父类
# 第一步-匹配被修改物品是否存在
class change1_type:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('物品交换系统-用户版-输入更改前信息')
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

        tk.Button(self.page, text='修改', command=self.change).grid(row=5, column=1,pady=100)
        tk.Button(self.page, text='返回', command=self.back).grid(row=5,column=2,pady=50)

    # 打开对应json（父类中空实现）
    def read(self):
        pass

    # 写入对应json（父类中空实现）
    def write(self, json_content):
        pass

    # 匹配到物品，跳转物品新信息输入界面（父类中空实现）
    def change2(self):
        pass

    # 检查物品是否匹配，如匹配，则从原json中暂时删去
    def change(self):
        if self.name.get() and self.phone.get():
            flag = 0 # 标志是否匹配成功
            json_content = []
            with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
                text = f.read()
            self.types = json.loads(text)
            self.read()
            for c in self.contents:
                # 针对2项必填项：名称+手机号，进行匹配
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
                self.change2()
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
class change1_type1(change1_type):
    def __init__(self,master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/1.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/1.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

    def change2(self):
        change2_type1(self.root)

# 类型二-json2
class change1_type2(change1_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/2.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/2.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

    def change2(self):
        change2_type2(self.root)

# 类型三-json3
class change1_type3(change1_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/3.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/3.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

    def change2(self):
        change2_type3(self.root)

# 类型四-json4
class change1_type4(change1_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/4.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/4.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

    def change2(self):
        change2_type4(self.root)

# 类型五-json5
class change1_type5(change1_type):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def read(self):
        with open('../物品数据库/5.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)

    def write(self, json_content):
        with open('../物品数据库/5.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

    def change2(self):
        change2_type5(self.root)

if __name__ == '__main__':
    root = tk.Tk()
    change1_type1(master=root)
    root.mainloop()
