#-*- coding:utf-8 -*-
"""
统计单次个数
1. 去掉标点符和换行符，所有大写都转小写
2. 合并相同的单次，统计频率，按照词频排序
3. 输出
"""
import re

def parse(text):
    res={}
    new_text=re.sub(r"[^\w ]"," ",text).lower()
    text_word_list=new_text.split(" ")
    text_word_list=filter(None,text_word_list)
    for word in text_word_list:
        if word in res:
            res[word]+=1
        else:
            res[word]=1
    return sorted(res.items(),key=lambda x:x[1])
   
#文件较小时   
# with open("test_word.txt") as inf:
    # with open("out.txt","w") as outf:
        # for word,freq in parse(inf.read()):
            # outf.write("word={},freq={}\n ".format(word,freq ))

            #文件较大时的处理
            
            




