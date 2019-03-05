# -*- coding:utf-8 -*-
"""
列表：可变对象，相当于其他语言的数组，具有很多实用的方法
扩展及添加
 append()
 extend()
 insert()
删除
 remove()
 del l[n]
 pop()
获取
 l[n]
 l.index(m) 元素m的索引号
排序【在原列表上排序】
 l.sort(reverse=False) 
 l.reverse()翻转
切片：
 l[:]
其他：
 l.count(m) 元素m出现的次数
 深拷贝和浅拷贝
 深拷贝：[:]，浅拷贝，赋值的方式，仅仅是所有的复制
"""

testList = [1,2,4,6,8,43,2,56]
testList.extend([2])
print(testList)
testList.extend([4,5,7])
print(testList)
testList.insert(5,67)#0开始，5的位置前插入
print(testList)
testList.sort()#默认升序
print(testList)
newList=testList
newList.remove(8)
print(testList)
print(newList)
print(newList[1:5])#[A:B] 元素A到B-1