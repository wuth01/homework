#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from web.workweixin.page.login_page import LoginPage
from web.workweixin.page.register_page import RegisterPage
from web.workweixin.public.base_page import BasePage

class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/#index_topAnchor"
    # 进入登录页
    def goto_login(self):
        # click login
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return LoginPage
        return LoginPage(self.driver)
    # 进入注册页
    def goto_register(self):
        # click signup
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self.driver)
