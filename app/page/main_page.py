from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist_page import AddressListPage
from app.page.gongzuotai_page import gongZuoTai
from app.public.base_page import BasePage

class MainPage(BasePage):
    address_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_gongzuotai(self):
        self.find(MobileBy.XPATH,'//*[@text="工作台"]').click()
        return gongZuoTai(self.driver)
    def goto_message(self):
        """
        进入消息页
        """
        pass
    def goto_address(self):
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)