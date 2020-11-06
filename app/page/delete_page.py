from app.public.base_page import BasePage

class Delete_page(BasePage):
    def delete_member(self):
        self.find_by_scroll("删除成员").click()
        self.driver.find_element_by_xpath('//*[contains(@text,"确定")]').click()
        from app.page.addresslist_page import AddressListPage
        return AddressListPage()