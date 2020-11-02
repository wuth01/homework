import pytest
from hamcrest import *
from app.page.app import App
class Testdaka():

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_daka(self):
        value= self.main.goto_gongzuotai().outside_daka()
        assert_that(True,equal_to(value))


# if __name__=='__main__':
#     pytest.main()