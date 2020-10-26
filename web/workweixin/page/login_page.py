#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.workweixin.page.register_page import RegisterPage
from web.workweixin.public.base_page import BasePage


class LoginPage(BasePage):

    # 扫码
    def scan(self):
        pass

    # 进入到注册页面
    def goto_register(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)