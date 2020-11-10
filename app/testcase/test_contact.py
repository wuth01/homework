import pytest
import yaml
from app.page.app import App

class TestContact():
    def setup(self):
        self.app = App()
        self.main=self.app.start().goto_main()

    def teardown(self):
        self.app.stop()
    """
    添加联系人
    """
    def test_addcontact(self,name="",gender="",phoneunm=""):
        result = self.main.goto_address() \
            .click_addmember(). \
            add_member_menual(). \
            add_contact(name,gender,phoneunm)
        # assert '添加成功' == result

    """
    删除联系人
    """
    def test_deletemember(self,name=""):
        assert  "没有联系人" == self.main.goto_address().\
            goto_userinfo(name).\
            menu().\
            edit_member().\
            delete_member().goto_userinfo(name)