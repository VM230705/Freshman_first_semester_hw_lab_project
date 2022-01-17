import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = "https://geojango.com/pages/list-of-nba-teams"
html = urllib.request.urlopen(url).read()       #url存網址 html打開
soup = BeautifulSoup(html, "html.parser")
body_tag = soup.find("body")
arena_list = ["Arena Name:", "Arena Location:", "Seating Capacity:", "Opening Year:"]

#path
div_class_name_is_moved_by_drawer = body_tag.find("div", class_="is-moved-by-drawer")
div_class_name_shogun_root = div_class_name_is_moved_by_drawer.find("div", class_="shogun-root")
div_class_name_shg_c = div_class_name_shogun_root.find("div", class_="shg-c", id="s-ece35a86-0578-416c-bb6f-c7c0d3687f88")
div_class_name_shogun_table_wrapper = div_class_name_shg_c.find("div", class_="shogun-table-wrapper")
tbody_tag = div_class_name_shogun_table_wrapper.find("tbody")
span_tag = tbody_tag.find_all("span")


team_info = {}
team = []
info = []
item = {}
i = 0
print("NBA teams name:")
#key:team name, value:info
for content in span_tag:
    i += 1
    if i % 5 == 1:
        team_info.setdefault(content.get_text(),[])
        name = content.get_text()
        print(name)
    else:
        team_info[name].append(content.get_text())


flag,i = 0,0
while True:
    team_name = input("Enter the NBA team name you want to search:")
    for team in team_info:
        if team_name == team:
            for information in team_info[team]:
                print(arena_list[i] + information)
                if i == 1:
                    city = information
                i += 1
            flag = 1
    if flag == 1:
        break
    else:
        print("Wrong Name")

from PIL import Image
import requests
from io import BytesIO

key = "AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"

while True:
    print(city)
    c2 = input("See the location of the city press \"c\",Go back press\"b\",Quit press\"q\"")
    if c2 == "c":
        url = "https://maps.googleapis.com/maps/api/staticmap?center=USA&zoom=4&size=800x800&markers=" + city + "&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
        print(url)
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
        while True:
            try:
                zoom = int(input("To see more specific about the city by setting zoom\n"
                         "1: World 5: Landmass/continent 10: City 15: Streets  20: Buildings\n"
                         "Enter a number you want to set:"))
                url = "https://maps.googleapis.com/maps/api/staticmap?center=USA&zoom="+str(zoom)+"&size=800x800&markers=" + city + "&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                img.show()
                c3 = input("Continue press\"c\", Go back press\"b\", Quit press\"q\"")
                if c3 == "c":
                    continue
                elif c3 == "b":
                    break
                elif c3 == "q":
                    exit()
                else:
                    print("Please enter qualified character")
                    continue
            except ValueError:
                print("Wrong input")
                continue


    elif c2 == "b":
        break
    elif c2 == "q":
        exit()
    else:
        print("Please enter qualified character")
        continue

