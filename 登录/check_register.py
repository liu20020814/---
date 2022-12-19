import json

# 检查是否注册成功
class checkr:
    def __init__(self):
        # 读入用户数据
        with open('../账号数据库/users.json', mode='r', encoding='utf-8') as f:
            text1 = f.read()
        self.users = json.loads(text1)
        # 读入管理员数据
        with open('../账号数据库/need_approval.json', mode='r', encoding='utf-8') as f:
            text2 = f.read()
        self.need_a = json.loads(text2)

    # 检查是否能够注册（账号未注册+密码6位+信息无缺漏）
    def check_register(self, username, password, name, home, phone, email):
         if username:
            if name:
                if home:
                    if phone:
                        if email:
                            for user in self.users:
                                if username == user['username']:
                                    return False,'很抱歉，该账号已存在'
                            for na in self.need_a:
                                if username == na['username']:
                                    return False,'该账号的注册正在审核中，请等待审核结果~'
                            if len(password)!=6:
                                return False,'很抱歉，请输入长度为6位的密码'
                            return True,'注册成功'
                        else:
                            return False,'很抱歉，邮箱不能为空'
                    else:
                        return False, '很抱歉，手机号不能为空'
                else:
                    return False, '很抱歉，住址不能为空'
            else:
                return False, '很抱歉，姓名不能为空'
         else:
             return False,'很抱歉，账号不能为空'

cr = checkr()
if __name__=='__main__':
    print(cr.check_register('11','','','','',''))