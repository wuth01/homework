import shelve

from selenium import webdriver

from web.workweixin.page.main_page import MainPage
from web.workweixin.public.base_page import BasePage


class Cookielogin(BasePage):
    def logincookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db = shelve.open("../cookies")
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
            # print(cookie)
        self.driver.refresh()
        return MainPage()