from appium.webdriver.common.mobileby import MobileBy
import allure
def handle_black(func):
    def wrapper(*args, **kwarts):
        from app.public.base_page import BasePage
        isinstance: BasePage = args[0]
        try:
            result = func(*args, **kwarts)
            isinstance.error_num = 0
            return result
        except Exception as e:
            isinstance.driver.save_screenshot("tmp.png")
            with open("tmp.png","rb") as f:
                content = f.read()
            allure.attach(content,attachment_type = allure.attachment_type.PNG)
            if isinstance.error_num > isinstance.max_num:
                raise e
            isinstance.error_num += 1
            for black_ele in isinstance.black_list:
                ele = isinstance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    isinstance.driver.find_element(*black_ele).click()
                    return wrapper(*args, **kwarts)
            raise e
    return wrapper
