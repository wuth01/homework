import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from app.page.main_page import mainPage



class Testdaka():
    def setup(self):
        self.main=mainPage()
    def test_daka(self):
        assert self.main.goto_gongzuotai().daka()


# if __name__=='__main__':
#     pytest.main()