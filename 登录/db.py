import json

# 检查是否登录成功
class MysqlDatabases1:
    def __init__(self):
        # 读入用户数据
        with open('../账号数据库/users.json', mode='r', encoding='utf-8') as f:
            text1 = f.read()
        # 读入管理员数据
        with open('../账号数据库/admins.json', mode='r', encoding='utf-8') as f:
            text2 = f.read()
        self.users = json.loads(text1)
        self.admins = json.loads(text2)

    # 检查登录信息（账号和密码是否存在且匹配）
    def check_login(self, type, username, password):
         if type == '0': # 管理员类型
             for admin in self.admins:
                 if username == admin['admin name']:
                     if password == admin['password']:
                         return True, '管理员登录成功'
                     else:
                         return False, '登录失败，管理员密码错误'
             return False,'登录失败，管理员不存在'

         elif type== '1': # 用户类型
             for user in self.users:
                 if username == user['username']:
                     if password == user['password']:
                         return True, '用户登录成功'
                     else:
                         return False, '登录失败，用户密码错误'
             return False,'登录失败，用户不存在'

         else: # 输入了无效的身份类型
             return False,'请输入有效的身份类型：0或1'

db = MysqlDatabases1()
if __name__=='__main__':
    print(db.check_login('0','admin3','333'))
