#-*- coding:utf-8 -*-
import subprocess
order='adb logcat'
pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
for i in iter(pi.stdout.readline,'b'):
	print (i)
print("eeee")