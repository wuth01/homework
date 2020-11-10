#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 基类 ：最基本的方法， driver 实例化， find()等 常用的最基本的方法
import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from app.public.hand_black import handle_black

class BasePage():
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    """
    find方法黑名单
    """
    black_list = [(MobileBy.XPATH, '//*[@class="work"]'),(MobileBy.ID, 'com.tencent.wework:id/i63')]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver=driver

    def teardown(self):
        self.driver.quit()

    @handle_black
    def find(self, by, locator):
        logging.info(by)
        logging.info(locator)
        if locator is None:
            result= self.driver.find_element(*by)
        else:
            result= self.driver.find_element(by, locator)
        return result

    def find_and_click(self, by, locator):
        logging.info('click')
        self.find(by, locator).click()

    def finds(self, by, locator):
        logging.info(by)
        logging.info(locator)
        if locator is None:
            result= self.driver.find_element(*by)
        else:
            result= self.driver.find_elements(by, locator)
        return result

    def wait_for_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info('get_toast_text')
        result = self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    def dialog(self):
        for i in range(4):
            logging.info('=========click 允许===========')
            try:
                if ('允许' in self.driver.page_source or '始终允许' in self.driver.page_source):
                    self.driver.switch_to.alert.accept()
            except:
                pass
    """
    测试步骤文件封装
    """
    def parse_yaml(self, path, func_name):
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])
    """
    测试步骤文件解析
    """
    @handle_black
    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                locator = (step['by'], step['locator'])
                self.wait_for_click(locator).click()

