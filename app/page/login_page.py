from appium.webdriver.common.mobileby import MobileBy

from app.page.main_page import mainPage
from app.public.base_page import BasePage


class Login(BasePage):
    def weixin_login(self):
        self.find(MobileBy.XPATH, '//*[@text="微信登录"]').click()
        self.find(MobileBy.XPATH, '//*[@text="进入企业"]').click()
        return mainPage
