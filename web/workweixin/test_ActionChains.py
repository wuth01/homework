#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

"""
ActionChains只针对pc端模拟，无法对h5页面操作，touch_action支持h5
"""
class TestActionChains():
    def setup(self):
        #self.driver = webdriver.Chrome()
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def click(self, element):
        element_click = element
        action = ActionChains(self.driver)
        action.click(element_click)
        action.perform()
        sleep(3)
        return

    def doubleclick(self, element):
        element_doubleclick = element
        action = ActionChains(self.driver)
        action.double_click(element_doubleclick)
        action.perform()
        sleep(3)
        return

    def rightclick(self, element):
        element_rightclick = element
        action = ActionChains(self.driver)
        action.context_click(element_rightclick)
        sleep(1)
        action.perform()
        sleep(3)
        return

    # def test_case_click(self,element):
    #     element_click=element
    #     # element_doubleclick=self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
    #     # element_rightclick=self.driver.find_element_by_xpath('//input[@value="right click me"]')
    #     action=ActionChains(self.driver)
    #     action.click(element_click)
    #     # action.context_click(element_rightclick)
    #     # action.double_click(element_doubleclick)
    #     sleep(1)
    #     action.perform()
    #     sleep(1)
    #     return

    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        element_moveto = self.driver.find_element_by_id('s-usersetting-top')
        action=ActionChains(self.driver)
        action.move_to_element(element_moveto).perform()

        sleep(1)
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        sleep(1)
        element_drag=self.driver.find_element_by_id("dragger")
        element_drop=self.driver.find_element_by_xpath("//div[2]")
        action=ActionChains(self.driver)
        """
        方法1
        """
        # action.drag_and_drop(element_drag,element_drop).perform()
        # sleep(1)
        """
        方法2
        """
        # action.click_and_hold(element_drag).release(element_drop).perform()
        # sleep(1)
        """
        方法3
        """
        action.click_and_hold(element_drag).move_to_element(element_drop).release().perform()
        sleep(1)

    def test_sendkeys(self):
        # self.driver.get("http://sahitest.com/demo/label.htm")
        # name=self.driver.find_element_by_xpath("//html/body/label/input")
        # name.click()
        # action = ActionChains(self.driver)
        # action.send_keys("username").pause(1)
        # action.send_keys(Keys.SPACE).pause(1)
        # action.send_keys("Tom").pause(1)
        # action.send_keys(Keys.BACK_SPACE).perform()
        # sleep(2)
        self.driver.get("http://www.baidu.com")
        name = self.driver.find_element_by_xpath('//*[@class="soutu-btn"]')
        name.click()
        u = self.driver.find_element_by_xpath('//*[@class="upload-pic"]')
        u.send_keys(f'E:\Selenium_HomeWork\workweixin\qq.jpg')
        sleep(5)