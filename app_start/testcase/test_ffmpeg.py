import subprocess

from app_start.public.BasePage import BasePage
class Test_starttime(BasePage):
    def setup(self):
        globals()['result'] = self.get_Process_Activity()
        self.stop(*globals()['result'])
        self.screenrecord()

    def teardown(self):
        #subprocess.Popen("adb shell rm -rf /sdcard/test/*", shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        pass
    def test_ffmpeg(self):
        self.ffmpeg()