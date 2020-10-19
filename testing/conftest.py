#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

import pytest

from pythoncode.calculator import Calculator

@pytest.fixture(scope='module')
def cal():
    calc = Calculator()
    print("计算开始")
    yield calc
    print("计算结束")

@pytest.fixture(scope='module')
def login():
    username = "dd"
    print ("登录操作")
    yield username
    print ("登出操作")
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