"""
测试文件
test_*.py
*_test.py
测试用例识别
Test*类包含的所有test*_的方法（类中不能有_int_方法）
不在测试类中所有的test*_的方法
可移植性unittest框架的用例
执行
pytest解释器执行
终端执行
pytest -vs 文件名::类型::方法名
pytest -vs -x 文件名 一旦用例报错了 就停止执行
pytest -vs --maxfail=2 2条用例失败后停止运行
pytest --collect-only 收集用例

pytest/py.test
pytest –v (最高级别信息–verbose) 打印详细运行日志信息
pytest -v -s 文件名 (s是带控制台输出结果，也是输出详细)
pytest 文件名.py 执行单独一个pytest模块
pytest 文件名.py::类名 运行某个模块里面某个类
pytest 文件名.py::类名::方法名 运行某个模块里面某个类里面的方法
pytest -x 文件名 一旦运行到报错，就停止 运行
pytest --maxfail=[num] 当运行错误达到num的时候就停止 运行
pytest -k "类名 and not 方法名” 执行某个关键字的用例
pytest -m [标记名] @pytest.mark.[标记名] 将运行有这个标记的测试用例
pytest --collect-only 收集用例按顺序执行
pytest - - junitxml=./result.xml 生成执行结果文件
pytest --setup-show 回溯fixture的执行过程
更多的用法使用pytest - -help查看帮助文档
pytest --last-failed 只运行上次失败的用例
pytest --failed-first 先运行上次失败的用例再运行成功的用例
"""
import pytest
class TestDemo:
    def test_demo(self):
        print ("demo")
def func(x):
    return x+1
def test_answer():
    assert func(4)==5
def test_answer1():
    assert func(3)==5
if __name__ == '__main__':
    pytest.main(['test_1.py::TestDemo','-v'])

def func(x):
    return x+1
def test_answer():
    assert func(4)==5