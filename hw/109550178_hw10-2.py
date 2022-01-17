import re
from urllib.request import Request, urlopen                         #為了解決403 Forbidden要import Request, urlopen
from bs4 import BeautifulSoup as soup                               #為了解決403 Forbidden 加上as soup
url = "https://www.ptt.cc/bbs/HCI/index20.html"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})           #為了解決403 Forbidden 加上這行
webpage = urlopen(req).read()                                       #為了解決403 Forbidden 加上這行
page_soup = soup(webpage, "html.parser")                            #為了解決403 Forbidden soup變成page_soup html變成webpage

titles = str(page_soup.find_all("div", class_="title"))                  #找到tag並轉換成string
title = list(re.findall(r"<a href=\"(.*)\">(.*)</a>", titles))           #title存放要取出的str
categories = []
for t in title:                                                     #用迴圈印出連結和標題
    print(t[0], t[1])
    categories += re.findall("\[.*]", str(t[1]))          #2        #catogories存放的標題前的類別

categories.sort()                                                   #排序
temp = ""                                                           #temp用來檢測是否重複出現過一樣的類別
dict = {}                                                           #dict的key存類別value存出現次數
for c in categories:
    if c != temp:                                                   #若該類別不曾出現過則執行
        pair = {c: categories.count(c)}                             #用pair接收新的類別和次數再update給dict
        dict.update(pair)
    temp = c
sorted_categories = sorted(dict.items(), key=lambda dict:dict[1], reverse=True)         #讓dict按照value的大小由大到小排序
for category in sorted_categories:
    print(category[0], ":", category[1])                            #一個一個印出類別和次數