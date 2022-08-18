#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import jieba.posseg
from pyperclip import copy
from bs4 import BeautifulSoup
import lxml,random



headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 5.1rv: 21.0) Gecko/20100101 Firefox/21.0'
    }

res = requests.get('http://baike.baidu.com',headers = headers)
res.encoding= 'utf-8'

soup = BeautifulSoup(res.text,'lxml')  
#print(soup.prettify())

item_list = []
item_url = {}

for i in soup.find_all(class_ = "content_tit"):
    #print(i)
    #item.append(str(i.span.string))
    #print(item)
    #print(i.span.string)
    item_list.append(i.span.string)
    
    m = i.find_parent('a')
    #print(m['href'])
    item_url[i.span.string] = m['href']
    #print()
#print('======')
#print(item_list,'\n',item_url)

item = random.choice(item_list)
url = item_url[item]
#url = 'https://baike.baidu.com/item/HarmonyOS%203'
response = requests.get(url,headers = headers)
response.encoding= 'utf-8'

text = BeautifulSoup(response.text,'lxml')
t = 0
for i in text.head.find_all('meta'):
    t+=1
    if t == 4:
        #print(i)
        des = i['content']
        l = des.split('。')
        description = l[0]
        #print(description)
        break
t = 0
for i in text.head.find_all('meta'):
    t+=1
    if t == 6:
        #print(i)
        more = i['content']
        
        #print(description)
        break


ch = input('type of xiaobian: ')
wo = random.choice(['不能吃','有毒','难以下咽','吃了对身体不好','伤肾','伤肝'])

if ch == '1':
    t = '观众朋友大家好，这里是田所营销号。近日，一外国小哥发现了5个{}的东西\n先说第一个，那就是大家都知道的{}。大家可能都很奇怪，{}怎么会{}呢？其实啊，小编也非常震惊，但是原因非常简单。\n{}相信大家都很熟悉，但{}{}是怎么回事呢？我们都知道，{}。那么，{}为什么{}呢？其实啊，就是因为{}，因此，{}才{}。大家听懂了吗？\n我是田所小编，我们下一期讲第二个{}的东西。欢迎点赞转发，关注我，每天一个趣味小知识，我们下期再见'.format(wo,item,item,wo,item,item,wo,description,item,wo,description,item,wo,wo)
    print(t)
    copy(t)

elif ch == '2':
    wf = jieba.posseg.cut(des+more)
    wl = []
    
    for word,flag in wf:
        
        print(flag)
        if flag == 'n' and word not in wl or flag == 'nl' and word not in wl:
            wl.append(word)
        

    t = '观众朋友大家好，这里是田所营销号。近日，一外国小哥发现了几个{}的东西，那么小编接下来给大家盘点这{}个{}的东西\n'.format(wo,len(wl),wo)
    for i in range(len(wl)):
        format_ = '第{}个，那就是大家都知道的{}。大家可能都很奇怪，{}怎么会{}呢？其实啊，小编也非常震惊，但是原因非常简单。\n{}相信大家都很熟悉，但{}{}是怎么回事呢？其实啊，就是因为{}吃了{}，所以{}才{}\n小编也非常震惊，你知道了吗？\n'.format(i+1,wl[i],wl[i],wo,wl[i],wl[i],wo,wl[i],random.choice(['不能吃','有毒','难以下咽','吃了对身体不好','伤肾','伤肝']),wl[i],wo)
        t = t+format_
    t = t+'欢迎点赞转发，关注我，每天一个趣味小知识，我们下期再见'
    print(t)
    copy(t)
else:
    pass


