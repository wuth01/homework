import yaml
from appium import webdriver
from app.page.main_page import  MainPage
from app.public.base_page import BasePage

with open('../datas/caps.yml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']

"""
存放app相关操作
比如启动应用，重启应用，停止应用，进入首页
"""
class App(BasePage):
    def start(self):
        if self.driver==None:
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self
    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass
    def stop(self):
        self.driver.quit()
    def goto_main(self)->MainPage:
        return MainPage(self.driver)