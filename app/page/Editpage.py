from app.page.delete_page import Delete_page
from app.public.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class Editpage(BasePage):
    def edit_member(self):
        locator = (MobileBy.XPATH,'//*[contains(@text,"设置备注和描述")]')
        ele = self.wait_for_click(locator)
        ele.click()
        self.find(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        return Delete_page(self.driver)