from web.workweixin.page.cookie_login import Cookielogin


class TestWX:
    def setup(self):
        self.login = Cookielogin()

    def test_imort_success(self):
        # assert self.index.goto_login().goto_register().register()
        text = self.login.logincookies().goto_TestImport().import_success()
        assert "导入成功1人"== text

    def test_import_fail1(self):
        text =self.login.logincookies().goto_TestImport().import_fail1()
        assert "批量导入模板错误" == text

    def test_import_fail2(self):
        text=self.login.logincookies().goto_TestImport().import_fail2(filename="",text="")
        assert "无变化1人" == text

