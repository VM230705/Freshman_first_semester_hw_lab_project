import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = "https://www.nba.com/schedule"
html = urllib.request.urlopen(url).read()       #url存網址 html打開
soup = BeautifulSoup(html, "html.parser")
section_tag = soup.find("section", class_="Block_tag__s36Yi")
div_tag = section_tag.find_all("div")

h2_tag = section_tag.find_all("h2")
print(h2_tag)