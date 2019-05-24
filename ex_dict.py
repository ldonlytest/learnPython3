#-*- coding:utf-8 -*-
"""
字典与集合
 无序元素的组合，键和值可以是混合型类型
 集合与字典唯一区别：集合无key-value键值配对
 高效：查找、删除、插入
 
 内部结构为一张哈希表
"""

#创建字典
ds={"name":"hapi","age":12}
ds1=dict([("name","hapi"),("age",12)])#序列形式
ds2=dict(name="hapi",age=12) #**kwargs形式

#创建集合
s1={1,2,3}
s2=set([1,2,3,4]) #序列形式

#集合不支持索引，不同列表，因为本质是一个哈希表

#判断一个元素是否在字典/集合中,注意字典默认是对比key
if  1 in s2:
	print("集合中存在")
if "age" in ds:
	print("字典中存在")
	
if "age" in ds.keys():
	print("字典中存在")
	
if 12 in ds.values():
	print("字典中值存在")
	
#集合/字典的增加、删除、更新

#字典
testdict={"name":"test","age":12}
#增加
testdict["height"]=166
print(testdict)
#更新
testdict["name"]="test1"
print(testdict)
#删除,pop,需要指定key,返回删除的value
print(testdict.pop("name"))
print(testdict)
print(testdict.popitem())#与pop类似,随机删除,这里返回是key-value
print(testdict)

#集合
ss={1,2,3,4,5}
#增加
ss.add(7)
ss.add(3) #重复的不会添加
print(ss)
#删除
ss.remove(1)
print(ss)

#排序
#字典，根据key或value进行排序
sortDist={"name":1,"age":12,"height":150}
print(sortDist.items()) #dict_items([('age', 12), ('name', 'test'), ('height', 150)]) 得到一个序列
print(sorted(sortDist.items(), key = lambda x: x[0])) #排序后得到一个包含元组的列表
print(sortDist)
print(sorted(sortDist.items(),key = lambda x: x[1])) #默认是升序，注意value不是同类型会报错

#集合
ss1={1,2,54,3}
print(sorted(ss1))#返回一个列表

sortDist={"name":1,"age":12,"height":150,['education']:["ss","sss"]}
print(sortDist)


