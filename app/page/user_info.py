from appium.webdriver.common.mobileby import MobileBy

from app.page.Editpage import Editpage
from app.public.base_page import BasePage


class Userinfo(BasePage):
    def menu(self):
        self.find(MobileBy.XPATH,'//*[@text="个人信息"]/../../../../..//android.widget.RelativeLayout').click()
        return Editpage(self.driver)