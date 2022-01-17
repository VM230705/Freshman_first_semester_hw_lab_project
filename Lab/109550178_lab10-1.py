import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = "https://www.goldenhorse.org.tw/awards/nw/?serach_type=award&sc=8&search_regist_year=2020&ins=49&fbclid=IwAR3VoyU7pgg7Mlg7oP219dOXmM3R3p23FyTNxpx7TLaK1hzKu9iXPjIjil0"
html = urllib.request.urlopen(url).read()       #url存網址 html打開
soup = BeautifulSoup(html, "html.parser")       #解析html
th_tag = soup.find_all("th")                    #找到所有<th>(所有獎項名都有的tag)
a_tag = soup.find_all("a")                      #找到所有<a>(有<th>但不是獎項名的項目)
f = 1
awards = []                 #創建list
for t in th_tag:
    for a in a_tag:         #用兩層迴圈判斷<a>是否在<th>內
        if a in t:          #若是 則讓f=0以此判斷
            f = 0
    if f == 1:              #若f==1則把獎項名加到awards裡去
        awards.append(t.get_text())         #用get_text得到tag的內容
print(awards)