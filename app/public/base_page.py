#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 基类 ：最基本的方法， driver 实例化， find()等 常用的最基本的方法
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver=driver

    def teardown(self):
        self.driver.quit()

    def find(self, by, locator):
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        logging.info(by)
        logging.info(locator)
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        logging.info('click')
        self.find(by, locator).click()

    def wait_for_click(self, locator, timeout=10):
        element= WebDriverWait(self.driver, timeout).until(
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
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
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
