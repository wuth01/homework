import pytest
@pytest.fixture(scope='module')
def status():
    print("计算开始")
    yield
    print("计算结束")

@pytest.fixture(scope='module')
def login():
    username = "dd"
    print ("登录操作")
    yield username
    print ("登出操作")