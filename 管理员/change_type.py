import json

# 修改物品类型
class changet:
    def __init__(self):
        pass

    # 修改物品类型
    def change_type(self, type1, type2):
        json_content = []
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)
        flag = 0 # 是否修改成功的标志
        for c in self.contents:
            ob = {}
            # 如果找到待修改的类型，则修改
            if type1 == c['type']:
                ob['type'] = type2
                flag=1
            else:
                ob['type'] = c['type']
            ob['num'] = c['num']
            ob['p1'] = c['p1']
            ob['p2'] = c['p2']
            ob['p3'] = c['p3']
            json_content.append(ob)
        if flag:
            with open('../物品数据库/types.json', mode='w', encoding='utf-8') as f:
                json.dump(obj=json_content, ensure_ascii=False, fp=f)
            return True, '修改成功'
        else:
            return False,'很抱歉，修改前的类型不存在'


ct = changet()
if __name__=='__main__':
    pass