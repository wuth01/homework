#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
import yaml
import allure

def get_Add_Datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']

    return [add_datas,add_ids]

def get_Sub_Datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    sub_datas = datas['sub']['datas']
    sub_ids = datas['sub']['ids']
    return [sub_datas,sub_ids]

def get_Mul_Datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    mul_datas = datas['mul']['datas']
    mul_ids = datas['mul']['ids']
    return [mul_datas,mul_ids]

def get_Div_Datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']
    return [div_datas,div_ids]

class TestCalc():
    # def setup_class(self):
    #     self.calc = Calculator()

    # def teardown_class(self):
    #     print("计算结束")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect',get_Add_Datas()[0],ids=get_Add_Datas()[1])
    def test_add(self,cal,a,b,expect):
        result = cal.add(a,b)
        assert round(result,2)==expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_Div_Datas()[0], ids=get_Div_Datas()[1])
    def test_div(self, cal, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                result = cal.div(a, b)
                print(result)
        else:
            result = cal.div(a, b)
            assert round(result, 2) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect',get_Sub_Datas()[0],ids=get_Sub_Datas()[1])
    def test_sub(self,cal,a,b,expect):
        result = cal.sub(a, b)
        assert round(result,2) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect',get_Mul_Datas()[0],ids=get_Mul_Datas()[1])
    def test_mul(self,cal,a,b,expect):
        result = cal.mul(a,b)
        assert round(result,2) == expect

if __name__ == '__main__':
    pytest.main(['test_calc.py','-v'])