import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
url = "https://www.goldenhorse.org.tw/awards/nw/?serach_type=award&sc=8&search_regist_year=2020&ins=49&fbclid=IwAR3VoyU7pgg7Mlg7oP219dOXmM3R3p23FyTNxpx7TLaK1hzKu9iXPjIjil0"
html = urllib.request.urlopen(url).read()       #url存網址 html打開
soup = BeautifulSoup(html, "html.parser")       #解析html
content = soup.get_text()                       #讓content=soup裡的文字
lyrics = re.findall(r"(詞.+?)\xa0.+?(曲.+?)\xa0.+?(唱.+?)(\(.+?\))", content)
s = list(lyrics)                   #用regular expression得到詞,曲,唱,電影名並存進list裡的tuple再轉成list
i = 0
for x in s:
    if i > 4:                       #用迴圈把要求的output印出
        break
    print(x[3])
    print(x[0])
    print(x[1])
    print(x[2])
    i += 1