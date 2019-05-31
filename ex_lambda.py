#-*- coding:utf-8 -*-
"""
匿名函数：lambda
一行简单的表达，不能扩展多行，能完成def 函数不能完成的事
函数式编程：代码中的每一块都是不可变的，都是由纯函数形式组成。
    纯函数：函数本身独立、互不影响，相同的输入，相同的输出
函数式编程：常用map、filter、reduce
"""
from functools import reduce 
#计算列表中每个数的平方,lambda 返回一个函数对象
print([(lambda x:x*x)(x) for x in range(10)])

"""
python中常见的函数式编程函数：
map(function,sequence) 对sequence中的每个元素，均运用function 函数
filter(function,sequence) 对sequence中的每个元素，均运用function 判断，返回true元素组成的数组
reduce(function,sequence) 对sequence中的每个元素进行乘积，即计算列表元素的累计积
  先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
"""

print(map(lambda x:x**2,range(10)))#结果是生成器

print(filter(lambda x:x%2==0,range(10))) #结果是生成器

print(reduce(lambda x,y:x*y,range(10)))

d={'mike':10,'lucy':2,'ben':30}
#根据值排序.默认升序
print(sorted(d.items(),key=lambda x:x[1],reverse=True))


