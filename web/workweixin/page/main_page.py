from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.workweixin.page.AddMemberPage import AddMemberPage
from web.workweixin.page.import_menmber import TestImport
from selenium.webdriver.common.by import By
from web.workweixin.public.base_page import BasePage
"""
获取导入通讯录按钮
"""
def contacts(self):
    btn_import = self.driver.execute_script('return document.getElementsByClassName("index_service_cnt_itemWrap")[1]')
    return btn_import
"""
获取添加联系人按钮
"""
def add_member(self):
    btn_add =  self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")
    return btn_add

class MainPage(BasePage):
    # base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 添加联系人
    def goto_addmember(self):
        # click addmember
        # 直接在首页点击【添加联系人】
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        # 点击 【联系人】
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        # sleep(2)
        # 点击 【添加联系人】按钮
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")

        # element:WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element = self.wait_for_click(locator)
        # element.click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)

    def goto_TestImport(self):
        sleep(2)
        contacts(self).click()
        return TestImport()