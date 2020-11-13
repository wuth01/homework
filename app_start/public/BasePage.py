import logging
import os
import subprocess
from time import sleep

import pytest

"""
app信息
获取当前界面元素：adb shell dumpsys activity top
获取任务列表：adb shell dumpsys activity activities
app入口
adb logcat|grep -i dispalyed
aapt dump badging mobile.apk | grep launchable-activity
apkanalyzer 最新版本sdk中才有
启动应用
adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S

"""
class BasePage():
	root_logger = logging.getLogger()
	print(f"root_logger.handlers:{logging.getLogger().handlers}")
	for h in root_logger.handlers[:]:
		root_logger.removeHandler(h)
	logging.basicConfig(level=logging.INFO)
	def get_Process_Activity(self):
		a='launcher'
		date = os.popen("adb shell dumpsys window | findstr mCurrentFocus","r")#获取当前运行的进程和activity
		mCurrentFocus = date.read()#读取date并赋值给mCurrentFofus
		date.close()
		list1 = mCurrentFocus.split(' ')
		list2 = list1[-1]
		list3 = list2.split('/')
		process = list3[0]#拿到包名
		list4 = list3[-1]
		list5 = list4.split('}')#拿到activity
		activity=list5[0]
		"""
		通过命令杀进程或者清除数据
		"""
		return (process,activity)

	def stop(self,process,activity):
		logging.info(process)
		logging.info(activity)
		a = 'launcher'
		process = process
		if a in activity:#通过和activity对比判断当前是否在桌面
			print("e")
		else:
			os.system("adb shell am force-stop "+ process)#不在桌面执行杀进程
			# os.system("adb shell pm clear "+ process)
	def clear(self,process,activity):
		logging.info(process)
		logging.info(activity)
		a = 'launcher'
		process = process
		if a in activity:  # 通过和activity对比判断当前是否在桌面
			print("e")
		else:
			os.system("adb shell pm clear " + process)  # 不在桌面执行杀进程清除数据

	def start(self, package,activity):
		logging.info(package)
		logging.info(activity)
		command = f"adb shell am start -S -W {package}/{activity}"
		subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	def screenrecord(self):
		command = "adb shell screenrecord --bugreport --time-limit 20 /sdcard/test/test.mp4 &"
		subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		sleep(20)
		os.system("adb pull /sdcard/test/test.mp4 .")
		sleep(10)
	def ffmpeg(self):
		# command = "ffmpeg -i test.mp4 test.gif"
		command = "ffmpeg -i test.mp4 -r 10 frames_%03d.jpg"
		os.system(command)