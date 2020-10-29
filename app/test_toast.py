import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'PBV0217210001983'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        # desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceIntialization'] = 'true'
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['uiautomationName'] = 'uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_toastr(self):
        views_ele=self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("Views").'
                                                        'instance(0));')
        views_ele.click()
        popup_ele=self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("Popup Menu").'
                                                        'instance(0));')
        popup_ele.click()
        make_ele=self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!")
        make_ele.click()
        search_ele=self.driver.find_element_by_xpath("//*[@text='Search']")
        search_ele.click()
        # print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text)

if __name__=='__main__':
    pytest.main()