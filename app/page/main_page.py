from appium.webdriver.common.mobileby import MobileBy

from app.page.gongzuotai_page import gongZuoTai
from app.public.base_page import BasePage

class mainPage(BasePage):
    def goto_gongzuotai(self):
        self.find(MobileBy.XPATH,'//*[@text="工作台"]').click()
        return gongZuoTai()