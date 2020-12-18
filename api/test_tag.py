import datetime
import pytest


# done: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# done: 代码冗余，需要封装
# done: 无法清晰的描述业务
# done: 使用jsonpath表达更灵活的递归查找
from jsonpath import jsonpath

from api.tag import Tag

class TestTag:
    def setup_class(self):
        self.tag = Tag()
    def teardown_class(self):
        pass
    def setup(self):
        pass
    def teardown(self):
        pass
    @pytest.mark.parametrize("group_name, tag_name,order", [
        ['测试','test1', 1],
        ['测试','test2', 2],
        ['客户等级', '1级', 1],
        ['客户等级', '2级', 2]
    ])
    def test_add_list(self,group_name, tag_name, order):
        group_name=group_name
        tag = [{"name": tag_name, "order": order}]
        r = self.tag.add(group_name=group_name,tag=tag)
        result = r
        assert result == tag_name

    @pytest.mark.parametrize("group_name, name,order", [
        ['测试', 'ddddddddddddddddddddddddddddddd', 1]
    ])
    def test_add_list_fail(self, group_name, name, order):
        group_name = group_name
        tag = [{"name": name, "order": order}]
        r = self.tag.add_fail(group_name=group_name, tag=tag)
        assert 'tag.name exceed max utf8 words 30' in r.json()['errmsg']

    @pytest.mark.parametrize("group_name,tag_name,i", [
        ['测试','tag1_new_',0],
        ['客户等级','tag1——中文',0],
        ['测试','tag1[中文]',1],
        ['客户等级', 'tag2——abcDE d', 1]
    ])
    def test_tag_update_list(self, group_name,tag_name,i):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        tag_id = self.tag.get_tag_id(group_name)[i]#改第i个标签名字
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]

        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # assert tags != []

    @pytest.mark.parametrize("group_name,tag_name", [
        ['测试','DFDASFSDFDSAFADSFDSAF'],
        ['客户等级','DFDASFSDFDSAFADSFDSAF']
    ]
    )
    def test_tag_update_list_fail(self,group_name,tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        tag_id = self.tag.get_tag_id(group_name)
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        assert "name exceed max utf8 words 30" in r.json()['errmsg']

    def test_del_tagid_all(self):
        group_name = self.tag.get_group_name()
        for i in group_name:
            tag_id = self.tag.get_tag_id(group_name=i)
            r = self.tag.delete_tag_id(tag_id)
            assert r['errcode'] == 0
            assert r['errmsg'] == 'ok'

if __name__ == '__main__':
    pytest.main(['test_tag.py','-v'])