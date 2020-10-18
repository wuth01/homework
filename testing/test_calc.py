import pytest

from pythoncode.calculator import Calculator

class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")
    # def setup(self):
    #     print("开始计算")
    # def teardown(self):
    #     print("计算结束")

    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 2],
                             [100, 100, 200]
                             ])
    def test_add_int(self,a,b,expect):
            result=self.calc.add(a,b)
            assert result==expect

    @pytest.mark.parametrize('a,b,expect',[
                              [0.1, 0.2, 0.3],
                              [0, 0.1, 0.1],
                            ])
    def test_add_float(self,a,b,expect):
            result=self.calc.add(a,b)
            assert round(result,1)==expect

    @pytest.mark.parametrize('a,b,expect',
                            [[1, 1, 1],
                            [100, 100, 1],
                            [0, 0.1, 0],
                            [2,0.1,20],
                            [0.5,10,0.05],
                            [2,3,0.67]
                             ])
    def test_div(self,a,b,expect):
            result = self.calc.div(a,b)
            assert round(result,2)== expect

    @pytest.mark.parametrize('a,b,expect',
                             [
                              [1, 0, 0]
                              ])
    def test_div_zero(self,a,b,expect):
        with pytest.raises(ZeroDivisionError):
            result=self.calc.div(a,b)
            print(result)
if __name__ == '__main__':
    pytest.main(['test_calc.py','-v'])