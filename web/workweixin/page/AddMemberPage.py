#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from web.workweixin.public.base_page import BasePage

class AddMemberPage(BasePage):

    def add_member(self, username, account, phonenum):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # sleep(2)
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return True

    def add_same_acount(self,username, account, phonenum):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # sleep(2)
        text = self.find(By.XPATH,'//*[@class="member_edit_item member_edit_item_Account"]//*[@class="ww_inputWithTips_tips"]').text
        print(text)
        return text
    def add_same_phonenum(self,username, account, phonenum):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # sleep(2)
        text = self.find(By.XPATH,'//*[@class="member_edit_sec"][2]//*[@class="member_edit_item_right ww_inputWithTips_WithErr"]//*[@class="ww_inputWithTips_tips"]').text
        print(text)
        return text

    def get_member(self, value):
        total_list=[]
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            total_list = total_list + titlelist
            print(len(total_list),total_list)
            if value in total_list:
                break
            result: str = self.find(By.CSS_SELECTOR,".ww_pageNav_info_text").text
            num, total = result.split('/', 1)
            if int(num) == int(total):
                break
            else:
                self.find(By.CSS_SELECTOR,".ww_commonImg_PageNavArrowRightNormal").click()
        return total_list