import json

# 添加物品类型
class addt:
    def __init__(self):
        pass

    # 添加类型
    def add_type(self ,type, p1=0, p2=0, p3=0):
        json_content = []
        with open('../物品数据库/types.json', mode='r', encoding='utf-8') as f:
            content = f.read()
        self.contents = json.loads(content)
        # 读入json中原有数据
        for c in self.contents:
            ob = {}
            ob['num'] = c['num']
            ob['type'] = c['type']
            ob['p1'] = c['p1']
            ob['p2'] = c['p2']
            ob['p3'] = c['p3']
            json_content.append(ob)
        # 最多5种物品类型，判断是否超出数量
        if len(self.contents) ==5:
            return False
        # 添加新数据
        object = {}
        object['num'] = len(self.contents)+1
        object['type'] = type
        object['p1'] = p1
        object['p2'] = p2
        object['p3'] = p3
        json_content.append(object)

        with open('../物品数据库/types.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=json_content, ensure_ascii=False, fp=f)
        return True

at = addt()
if __name__=='__main__':
    pass