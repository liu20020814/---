import json

# 写入注册
class writer:
    def __init__(self):
        pass

    # 写入注册
    def write_register(self,username, password, name, home, phone, email):
        json_content = []
        with open('../账号数据库/need_approval.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)
        # 读入json原有数据
        for c in self.contents:
            ob = {}
            ob['username'] = c['username']
            ob['password'] = c['password']
            ob['name'] = c['name']
            ob['home'] = c['home']
            ob['phone'] = c['phone']
            ob['email'] = c['email']
            json_content.append(ob)
        # 添加新数据
        object = {}
        object['username'] = username
        object['password'] = password
        object['name'] = name
        object['home'] = home
        object['phone'] = phone
        object['email'] = email
        json_content.append(object)

        with open('../账号数据库/need_approval.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)

wr = writer()
if __name__=='__main__':
    pass