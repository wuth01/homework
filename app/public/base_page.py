#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 基类 ：最基本的方法， driver 实例化， find()等
import logging

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'PBV0217210001983'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = 'com.tencent.wework.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceIntialization'] = 'true'
        # desired_caps['settings[waitForIdleTimeout]'] = 0
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['uiautomationName'] = 'uiautomator2'
        desired_caps['newCommandTimeout'] = '2000'
        if driver == None:
            #第一次初始化
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element= WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element
    def dialog(self):
        for i in range(4):
            logging.info('=========click 允许===========')
            try:
                if ('允许' in self.driver.page_source or '始终允许' in self.driver.page_source):
                    self.driver.switch_to.alert.accept()
            except:
                pass
