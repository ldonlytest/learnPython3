#-*- coding:utf-8 -*-
"""
条件与循环
"""
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
               ['mike', '1999-01-01', 'male'],
               ['nancy', '2001-02-01', 'female']]

               
#多行
res=[]
for  value in values:
    if len(attributes)!=len(value):
        continue
    temp={}
    for  index,each in enumerate(value):
        temp[attributes[index]]=each
    res.append(temp)
print(res)

#使用zip
s=[dict(zip(attributes,value)) for  value  in  values if len(attributes)==len(value)]
