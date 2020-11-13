#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import signal
import subprocess
from typing import List
import pytest

@pytest.fixture(scope='session',autouse=True)
def status():
    print("开始测试")
    yield
    print("结束测试")

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """
    用例结果显示汉字
    """
    for item in items:

        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf8').decode('unicode-escape')

@pytest.fixture(scope='session',autouse=False)
def record_vedio():
    command = "scrcpy --record test.mp4"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)

# def get_time():
#     command = "adb logcat | findstr -i displayed"
#     p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     yield
#     # os.kill(p.pid, signal.CTRL_C_EVENT)
#     print(p)
