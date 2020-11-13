from app_start.public.BasePage import BasePage
class Test_starttime(BasePage):
    def setup(self):
        globals()['result'] = self.get_Process_Activity()
        self.stop(*globals()['result'])

    def teardown(self):
        pass

    def test_get_start_time(self):
        package = 'com.sina.weibo'
        activity = 'com.sina.weibo.account.login.LoginActivity'
        self.start(package,activity)
