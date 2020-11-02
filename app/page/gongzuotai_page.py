from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from app.public.base_page import BasePage

class gongZuoTai(BasePage):
    def outside_daka(self):
        self.find_by_scroll('打卡').click()
        self.driver.update_settings({"waitForIdleTimeout": 0})
        locator=(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/hxb"]')
        ele= self.wait_for_click(locator)
        print(ele.get_attribute('clickable'))
        self.find(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.find(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        # 显式等待
        ele1=WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        return ele1
