# -*- coding:utf-8 -*-

tabby_cat = "\t T'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(20*'*') #注意后面是字符
print("this is result:%s"%tabby_cat)#会将转义符转义
print("this is result:%r"%tabby_cat)#按照原串输出