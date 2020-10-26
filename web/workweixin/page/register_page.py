#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from web.workweixin.public.base_page import BasePage
class RegisterPage(BasePage):
    # 注册信息
    def register_success(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("aaaaa")
        self.driver.find_element(By.ID, "manager_name").send_keys("bbbbbb")
        self.driver.find_element(By.ID, "register_tel").send_keys("13900000000")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
    def register_fail(self):
        self.find(By.ID, "corp_name").send_keys("aaaaa")
        self.find(By.ID, "manager_name").send_keys("bbbbbb")
        self.find(By.ID, "register_tel").send_keys("13900000000")
        self.find(By.ID, "submit_btn").click()
        return True