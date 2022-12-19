import tkinter as tk
import json

# 审核注册
class check:
    def __init__(self, master:tk.Tk):
        #页面布局
        self.root = master
        self.root.title('审核注册')
        self.root.geometry('400x380')

        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)

        with open('../账号数据库/need_approval.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.need_a = json.loads(text)
        # 尚无需要审核的信息
        if len(self.need_a)==0:
            tk.Label(self.page, text='尚无需要审核的注册信息').grid(row=1, column=1, pady=10)
            tk.Label(self.page, text='休息一下吧~').grid(row=2, column=1, pady=10)
            tk.Button(self.page, text='返回', command=self.back).grid(row=7, column=3, padx=40)
        # 有需要审核的信息
        else:
            tk.Label(self.page, text='账号：').grid(row=1, column=1, pady=10)
            tk.Label(self.page, text='密码：').grid(row=2, column=1, pady=10)
            tk.Label(self.page, text='姓名：').grid(row=3, column=1, pady=10)
            tk.Label(self.page, text='住址：').grid(row=4, column=1, pady=10)
            tk.Label(self.page, text='手机号：').grid(row=5, column=1, pady=10)
            tk.Label(self.page, text='邮箱：').grid(row=6, column=1, pady=10)
            tk.Button(self.page, text=' ✔', command=self.yes).grid(row=7, column=1, padx=40,pady=10)
            tk.Button(self.page, text='❌', command=self.no).grid(row=7, column=2,padx=40)
            tk.Button(self.page, text='返回', command=self.back).grid(row=7, column=3,padx=40)

            tk.Label(self.page, text=self.need_a[0]['username']).grid(row=1, column=2, pady=10)
            tk.Label(self.page, text=self.need_a[0]['password']).grid(row=2, column=2, pady=10)
            tk.Label(self.page, text=self.need_a[0]['name']).grid(row=3, column=2, pady=10)
            tk.Label(self.page, text=self.need_a[0]['home']).grid(row=4, column=2, pady=10)
            tk.Label(self.page, text=self.need_a[0]['phone']).grid(row=5, column=2, pady=10)
            tk.Label(self.page, text=self.need_a[0]['email']).grid(row=6, column=2, pady=10)

    # 审核通过：从need_approval.json中删除，并添加到users.json中
    def yes(self):
        json_content = []
        with open('../账号数据库/users.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)
        for c in self.contents:
            ob = {}
            ob['username'] = c['username']
            ob['password'] = c['password']
            ob['name'] = c['name']
            ob['home'] = c['home']
            ob['phone'] = c['phone']
            ob['email'] = c['email']
            json_content.append(ob)
        object = {}
        object['username'] = self.need_a[0]['username']
        object['password'] = self.need_a[0]['password']
        object['name'] = self.need_a[0]['name']
        object['home'] = self.need_a[0]['home']
        object['phone'] = self.need_a[0]['phone']
        object['email'] = self.need_a[0]['email']
        json_content.append(object)
        with open('../账号数据库/users.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)
        self.no()

    # 审核不通过：从need_approval.json中删除
    def no(self):
        json_content = []
        i=1
        while(i<len(self.need_a)):
            ob = {}
            ob['username'] = self.need_a[i]['username']
            ob['password'] = self.need_a[i]['password']
            ob['name'] = self.need_a[i]['name']
            ob['phone'] = self.need_a[i]['phone']
            ob['home'] = self.need_a[i]['home']
            ob['email'] = self.need_a[i]['email']
            json_content.append(ob)
            i+=1
        with open('../账号数据库/need_approval.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)
        self.page.destroy()
        check(self.root)

    # 返回上一级
    def back(self):
        from 管理员.AdminPage import AdminPage
        self.page.destroy()
        AdminPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    check(master=root)
    root.mainloop()