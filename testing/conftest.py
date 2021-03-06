#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List
import pytest
import yaml

from pythoncode.calculator import Calculator

@pytest.fixture(scope='class', autouse=False)
def conn_db():
    print("完成 数据库连接")
    yield "database"
    print("关闭 数据库连接")

@pytest.fixture(scope='module')
def cal():
    calc = Calculator()
    print("计算开始")
    yield calc
    print("计算结束")

@pytest.fixture(scope='module', params=['tom', 'jerry'])
def login(request):
    # setup 操作
    print("登录操作")
    username = request.param
    # yield 相当于return 操作
    yield username
    # teardown操作
    print("登出操作")

"""
收集用例个性化制定用例
"""
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    print(type(items))
    """
    倒序执行用例
    """
    items.reverse()
    """
    用例结果显示汉子
    """
    for item in items:

        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf8').decode('unicode-escape')

    """
    用例加标签
    """
    if 'add' in item.name:
        item.add_marker(pytest.mark.add)
    elif 'div' in item.name:
        item.add_marker(pytest.mark.div)
    elif 'mul' in item.name:
        item.add_marker(pytest.mark.mul)
    elif 'sub' in item.name:
        item.add_marker(pytest.mark.sub)

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts-FIS")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')

    if myenv == 'test':
        datapath = "datas/test/data.yml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    print(datas)

    return myenv, datas