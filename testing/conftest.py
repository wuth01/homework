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