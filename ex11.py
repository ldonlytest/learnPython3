# -*- coding:utf-8 -*-

#print ("How old are you?")
age =  input("How old are you?") #python2是raw_input()
print("How tall are you?")
height = input() #从标准输入读入一行文本，默认标准输入是键盘
print("How much do you weigh?")
weight = input()

print ("So,you're %r old,%r tall and %r heavy."%(age,height,weight))

print(20*'#')
print("请输入一个数")
first_num= input()
print("请输入第二个数")
second_num=input()
print("计算2数之和%r"%(first_num+second_num)) #读入是字符类型
print("计算2数之和%d"%(int(first_num)+int(second_num)))