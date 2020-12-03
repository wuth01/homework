import datetime
import json

import pytest
import requests

# done: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# done: 代码冗余，需要封装
# done: 无法清晰的描述业务
# done: 使用jsonpath表达更灵活的递归查找
from jsonpath import jsonpath

from api.tag import Tag

class TestTag:
    def setup_class(self):
        self.tag = Tag()


    @pytest.mark.parametrize("group_name, name,order", [
        ['测试','test1', 1],
        ['测试','test2', 2],
        ['客户等级', '一级', 1]
    ])
    def test_add_list(self,group_name, name, order):
        group_name=group_name
        tag = [{"name": name, "order": order}]
        r = self.tag.add(group_name=group_name,tag=tag)
        tag_name = r[0]
        assert tag_name[0] == name

    @pytest.mark.parametrize("group_name, name,order", [
        ['测试', 'ddddddddddddddddddddddddddddddd', 1]
    ])
    def test_add_list_fail(self, group_name, name, order):
        group_name = group_name
        tag = [{"name": name, "order": order}]
        r = self.tag.add_fail(group_name=group_name, tag=tag)
        assert 'tag.name exceed max utf8 words 30' in r.json()['errmsg']

    @pytest.mark.parametrize("group_name,tag_name", [
        ['测试','tag1_new_'],
        ['客户等级','tag1——中文'],
        ['测试','tag1[中文]']]
    )
    def test_tag_update_list(self, group_name,tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        tag_id = self.tag.get_tag_id(group_name)[0]
        print(tag_id)
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

    @pytest.mark.parametrize("tag_name", [
        'DFDASFSDFDSAFADSFDSAF']
    )
    def test_tag_update_list_fail(self, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        tag_id = self.tag.get_tag_id()[0]
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        assert "name exceed max utf8 words 30" in r.json()['errmsg']

    @pytest.mark.parametrize("group_name", [
        '测试']
    )
    def test_del_list_all(self,group_name):
        tag_id = self.tag.get_tag_id(group_name)
        r = self.tag.delete(tag_id)
        r = self.tag.list()
        r = r.json()['tag_group']
        for i in r:
            if i['group_name'] == group_name:
                assert False
            else:
                assert True
