#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
编辑联系人页面
"""
import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from app.page.memberInviteMenuPage import MemberInviteMenuPage
from app.public.base_page import BasePage

def get_Add_Vale():
    with open("../datas/contact.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_vale = datas['add']
    return add_vale

class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def add_contact(self, name, gender, phoneunm):
        # 设置 【用户名】【性别】【手机号】
        for value in get_Add_Vale():
            name = value['name']
            gender = value['gender']
            phoneunm = value['phoneunm']
            self.find(By.XPATH,"//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
            self.find(By.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()

            if gender == "男":
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
                self.find(By.XPATH, "//*[@text='男']").click()
            else:
                self.find(By.XPATH, "//*[@text='女']").click()
            self.find(By.XPATH,
                      '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(phoneunm)
            # 点击【保存】
            self.find(By.XPATH, "//*[@text='保存']").click()
            from app.page.memberInviteMenuPage import MemberInviteMenuPage
            return MemberInviteMenuPage(self.driver)
