#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.page.memberInviteMenuPage import MemberInviteMenuPage
from app.page.user_info import Userinfo
from app.public.base_page import BasePage

class AddressListPage(BasePage):
    def click_addmember(self):
        # 滚动查找【添加成员】
        self.find_by_scroll("添加成员").click()

        return MemberInviteMenuPage(self.driver)
    def goto_userinfo(self,name):
        try:
            self.find_by_scroll(f"{name}").click()
            return Userinfo(self.driver)
        except:
            result="没有联系人"
            return result
