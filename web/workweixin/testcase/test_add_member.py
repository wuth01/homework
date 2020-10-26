from web.workweixin.page.cookie_login import Cookielogin
class TestWX:
    def setup(self):
        self.login = Cookielogin()

    def test_addmember_success(self):
        username = '吴天昊2'
        account = 'hogwarts'
        phonenum = '18811111111'
        addmember=self.login.logincookies().goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member(username)

    def test__same_acount(self):
        username = "aaaaaab"
        account = "fffffffff"
        phonenum = "13500000008"
        addmember = self.login.logincookies().goto_addmember()
        text= addmember.add_same_acount(username, account, phonenum)
        assert '该帐号已被“aaaaaab”占有' in text

    def test_same_phonenum(self):
        username = "aaaaaab"
        account = "fffffffff"
        phonenum = "13500000008"
        addmember = self.login.logincookies().goto_addmember()
        text = addmember.add_same_phonenum(username, account, phonenum)
        assert '该手机号已被“aaaaaab”占有' in text