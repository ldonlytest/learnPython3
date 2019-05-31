#-*- coding:utf-8 -*-
"""
函数
 模块重复使用、更有组织化
 知识点：
   1. 传参，类型是多态型，必要时需要检查
   2. 变量作用域，修饰词：global、nonlocal
   3. 嵌套函数 主要是保证内部函数隐私及效率，例如一些需要校验的字段，只需校验一次
   4. 闭包函数 ，使用形式链式的方式，可以提高程序的效率，减少重复代码，例如：重要参数是共用的
"""

#局部变量
def calc():
    pass

#全局变量,默认下可以使用，不可以更改，若需要更改，则global修饰
MIN_VALUE=1
def change():
    print(MIN_VALUE)
    
def change1():
    global MIN_VALUE
    MIN_VALUE+=1
    print(MIN_VALUE)
change()
change1()

#外部函数变量,默认下内部函数可使用外部函数变量，但是不可以更改，如要更改，则需要nonlocal修饰
def outer(text):
    outline=1
    def inner():
        print("line={},text={} ".format(outline,text))
    inner()
outer("we")
outer("are")
outer("famleee")

def outer1(text):
    outline=1
    def inner1():
        nonlocal outline
        outline+=1
        print("line={},text={} ".format(outline,text))
    inner1()
outer1("we")
outer1("are")
outer1("famleee")

#闭包函数
#一个数的n次幂
def nth_power(exp1):
    def exp(base):
        return exp1**base
    return exp
    
print(nth_power(2)(5))
print(nth_power(3)(5))
print(nth_power(4)(5))