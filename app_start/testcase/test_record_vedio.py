import subprocess
from time import sleep

from app_start.public.BasePage import BasePage
class Test_starttime(BasePage):
    def setup(self):
        globals()['result'] = self.get_Process_Activity()
        self.stop(*globals()['result'])
    def teardown(self):
        pass

    def test_record(self,record_vedio):
        sleep(10)
        return

    def test_pic(self):
        self.ffmpeg()

    def test_del(self):
        self.del_jpf()
        self.del_mp4()
