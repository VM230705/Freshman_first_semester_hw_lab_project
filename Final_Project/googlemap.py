import requests
import json
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#google map api
from PIL import Image
import requests
from io import BytesIO
import re
url3 = "https://nba.udn.com/nba/cate/6754"
html = urllib.request.urlopen(url3).read()       #url存網址 html打開
soup = BeautifulSoup(html, "html.parser")       #解析html
content = soup.get_text()

print(content)
news = re.findall("..hours ago.*?\.", content)
news.sort()
#news.insert(4,0)
for sentence in news:
    print(sentence)