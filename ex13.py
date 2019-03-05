# -*- coding:utf-8 -*-
from sys import argv
"""
参数、解包、变量
"""
script,first,second,third=argv #argv变量参数
print("The script is calling:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
print("input和argv联合使用")
one,two,three = input ("请出入三个数")
print(one,two,three)