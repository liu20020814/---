import tkinter as tk
import json
from 用户.add_item_page import add_type1,add_type2,add_type3,add_type4,add_type5
from 用户.show_item_page import show_type1,show_type2,show_type3,show_type4,show_type5
from 用户.search_item_page import search_type1,search_type2,search_type3,search_type4,search_type5
from 用户.delete_item_page import delete_type1,delete_type2,delete_type3,delete_type4,delete_type5
from 用户.change_item_page1 import change1_type1,change1_type2,change1_type3,change1_type4,change1_type5

# 所有选择功能操作的父类
class choose_type0:
    def __init__(self, master:tk.Tk):
        # 页面布局
        self.root = master
        self.root.title('选择物品类型')
        self.root.geometry('300x220')

        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)
        self.show_choice()
        tk.Button(self.page, text='返回', command=self.back).grid(row=4,column=2,pady=10)

    # 展示物品类型选项
    def show_choice(self):
        tk.Label(self.page, text='请先选择物品类型：').grid(row=1, column=1)
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)
        i = 1
        for c in self.contents:
            if i==1:
                self.b1=tk.Button(self.page, text=c['type'], command=self.turn_type1)
                self.b1.grid(row=2, column=1, padx=20, pady=10)
            elif i==2:
                self.b2=tk.Button(self.page, text=c['type'], command=self.turn_type2)
                self.b2.grid(row=2, column=2, padx=20, pady=10)
            elif i==3:
                self.b3=tk.Button(self.page, text=c['type'], command=self.turn_type3)
                self.b3.grid(row=3, column=1, padx=20, pady=10)
            elif i==4:
                self.b4=tk.Button(self.page, text=c['type'], command=self.turn_type4)
                self.b4.grid(row=3, column=2, padx=20, pady=10)
            elif i==5:
                self.b5=tk.Button(self.page, text=c['type'], command=self.turn_type5)
                self.b5.grid(row=4, column=1, padx=20, pady=10)
            i += 1

    # 返回上一级
    def back(self):
        from 用户.UserPage import UserPage
        self.page.destroy()
        UserPage(self.root)

    # 对不同类型物品操作的分支（父类中空实现）
    def turn_type1(self):
        pass

    def turn_type2(self):
        pass

    def turn_type3(self):
        pass

    def turn_type4(self):
        pass

    def turn_type5(self):
        pass

# 功能一-添加物品
class choose_type1(choose_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def turn_type1(self):
        self.page.destroy()
        add_type1(self.root)

    def turn_type2(self):
        self.page.destroy()
        add_type2(self.root)

    def turn_type3(self):
        self.page.destroy()
        add_type3(self.root)

    def turn_type4(self):
        self.page.destroy()
        add_type4(self.root)

    def turn_type5(self):
        self.page.destroy()
        add_type5(self.root)

# 功能二-搜索物品
class choose_type2(choose_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def turn_type1(self):
        self.page.destroy()
        search_type1(self.root)

    def turn_type2(self):
        self.page.destroy()
        search_type2(self.root)

    def turn_type3(self):
        self.page.destroy()
        search_type3(self.root)

    def turn_type4(self):
        self.page.destroy()
        search_type4(self.root)

    def turn_type5(self):
        self.page.destroy()
        search_type5(self.root)

# 功能三-显示物品
class choose_type3(choose_type0):
    def __init__(self, master:tk.Tk):
        super().__init__(master)

    def turn_type1(self):
        self.page.destroy()
        show_type1(self.root)

    def turn_type2(self):
        self.page.destroy()
        show_type2(self.root)

    def turn_type3(self):
        self.page.destroy()
        show_type3(self.root)

    def turn_type4(self):
        self.page.destroy()
        show_type4(self.root)

    def turn_type5(self):
        self.page.destroy()
        show_type5(self.root)

# 功能四-删除物品
class choose_type4(choose_type0):
    def __init__(self, master: tk.Tk):
        super().__init__(master)

    def turn_type1(self):
        self.page.destroy()
        delete_type1(self.root)

    def turn_type2(self):
        self.page.destroy()
        delete_type2(self.root)

    def turn_type3(self):
        self.page.destroy()
        delete_type3(self.root)

    def turn_type4(self):
        self.page.destroy()
        delete_type4(self.root)

    def turn_type5(self):
        self.page.destroy()
        delete_type5(self.root)

# 功能五-修改物品
class choose_type5(choose_type0):
    def __init__(self, master: tk.Tk):
        super().__init__(master)

    def turn_type1(self):
        self.page.destroy()
        change1_type1(self.root)

    def turn_type2(self):
        self.page.destroy()
        change1_type2(self.root)

    def turn_type3(self):
        self.page.destroy()
        change1_type3(self.root)

    def turn_type4(self):
        self.page.destroy()
        change1_type4(self.root)

    def turn_type5(self):
        self.page.destroy()
        change1_type5(self.root)


if __name__ == '__main__':
    pass