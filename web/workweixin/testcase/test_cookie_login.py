from web.workweixin.page.cookie_login import Cookielogin

class TestWX:
    def setup(self):
        self.login = Cookielogin()

    def test_cookielogin(self):
        # assert self.index.goto_login().goto_register().register()
        assert self.login.logincookies()