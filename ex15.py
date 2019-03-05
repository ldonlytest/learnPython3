# -*- coding:utf-8 -*-
from sys import argv
"""
文件读取
"""

script,file_name = argv
print("打开文件:%s"%open(file_name,"r").read())#open只返回一个文件对象
again_file=input("> ")

