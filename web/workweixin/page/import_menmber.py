from time import sleep
from web.workweixin.public.base_page import BasePage

"""
获取上传文件按钮
"""
def up_files(self):
    btn =self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_fileContainer_uploadInputMask"]')
    return btn
"""
获取上传的文件名
"""
def get_filename(self):
    filename = self.driver.find_element_by_css_selector(".ww_fileImporter_fileContainer_fileNames").text
    return filename

"""
提交按钮
"""
def submit(self):
    btn_submit = self.driver.find_element_by_xpath('//*[@class="qui_btn ww_btn ww_btn_Large ww_btn_Blue ww_fileImporter_submit"]')
    return btn_submit

class TestImport(BasePage):
    def import_success(self,filename,text):
        up_files(self).send_keys('E:\homework\web\workweixin\qqq.xlsx')
        sleep(3)
        filename=get_filename(self)
        submit(self).click()
        sleep(5)
        text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_successImportText"]').text
        return text

    def import_fail1(self,filename,text):
        up_files(self).send_keys('E:\homework\web\workweixin\qq.xls')
        sleep(3)
        filename = get_filename(self)
        submit(self).click()
        sleep(5)
        text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_errorTitle"]').text
        return text

    def import_fail2(self,filename,text):
        up_files(self).send_keys('E:\homework\web\workweixin\qqq.xlsx')
        sleep(3)
        filename = get_filename(self)
        submit(self).click()
        sleep(5)
        text = self.driver.find_element_by_xpath('//*[@class="ww_fileImporter_successImportText"]').text
        return text