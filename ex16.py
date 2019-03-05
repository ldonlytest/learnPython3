# -*- coding:utf-8 -*-
from sys import argv
"""
open
"""
script,filename=argv
print("We're going to erase %r."%(filename))
print("If you don't eant that ,hit CTR-C(^C)")
print("If you do want that,hit RETURN")
input("?")
print("Opening the file...")
target=open(filename,"w")
print("Truncating the file,Goodbye")
target.truncate()
print("Now I'm going to ask you for three lines")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")
print("I'm going to write these to the file")
target.write("%s\n%s\n%s"%(line1,line2,line3))
print("And finally,we close it.")
target.close()
print("Openging the file")
file=open(filename,"r")#访问模式 r w a，修饰符+,表示可同时读写
print(file.read())
print("Closing the file")
file.close()
