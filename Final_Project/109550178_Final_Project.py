#nba api
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import commonteamroster

#scrape
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#google map api
from PIL import Image
import requests
from io import BytesIO
key = "AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"

#regular expression
import re
url3 = "https://www.nba.com/news"
html = urllib.request.urlopen(url3).read()
soup = BeautifulSoup(html, "html.parser")
content = soup.get_text()
news = re.findall("\d* hours ago.*?\.", content)
news.sort()
print("NBA NEWS:")
for sentence in news:
    print(sentence)
print("\n\n")

arena_list = ["Arena Name:", "Arena Location:", "Seating Capacity:", "Opening Year:"]
while True:
    try:
        c1 = input("Search a player press \"p\".Search a team press \"t\"\n")

#查找球員(nba_api)
        if c1 == "p":
            team_dict = teams.get_teams()
            player_dict = players.get_active_players()

            player_name_list = []
            for player_name in player_dict:
                player_name_list.append(player_name["full_name"])
            player_name_list.sort()
            for player_name in player_name_list:
                print(player_name)

            flag = 0
            while True:
                player_name = input("Enter the NBA player you want to know:")
                for player in player_dict:
                    if player_name == player["full_name"]:
                        player_id = player["id"]
                        flag = 1
                if flag == 1:
                    break
                else:
                    print("Wrong Name!")
                    continue

            # Basic Request
            player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
            custom_headers = {
                'Host': 'stats.nba.com',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
            }
#球員個資(nba_api)
            info_dict = player_info.get_normalized_dict()
            print("BIRTHDATE:", info_dict["CommonPlayerInfo"][0]["BIRTHDATE"])
            print("SCHOOL:", info_dict["CommonPlayerInfo"][0]["SCHOOL"])
            print("COUNTRY:", info_dict["CommonPlayerInfo"][0]["COUNTRY"])
            print("HEIGHT:", info_dict["CommonPlayerInfo"][0]["HEIGHT"])
            print("WEIGHT:", info_dict["CommonPlayerInfo"][0]["WEIGHT"])
            print("SEASON_EXP:", info_dict["CommonPlayerInfo"][0]["SEASON_EXP"])
            print("POSITION:", info_dict["CommonPlayerInfo"][0]["POSITION"])
            print("TimeFrame:", info_dict["PlayerHeadlineStats"][0]["TimeFrame"])
            print("PTS:", info_dict["PlayerHeadlineStats"][0]["PTS"])
            print("AST:", info_dict["PlayerHeadlineStats"][0]["AST"])
            print("REB:", info_dict["PlayerHeadlineStats"][0]["REB"], "\n")

#球隊名單(nba_api)
            team_name = str(info_dict["CommonPlayerInfo"][0]["TEAM_CITY"] + " " + info_dict["CommonPlayerInfo"][0]["TEAM_NAME"])
            print(team_name + " Roster:")

            team_dict = teams.get_teams()
            for name in team_dict:
                if team_name == name["full_name"]:
                    team_id = name["id"]

            team_roster = commonteamroster.CommonTeamRoster(team_id=team_id, season="2020")
            for info in team_roster.get_normalized_dict()["CommonTeamRoster"]:
                print(info["PLAYER"] + " : " + info["POSITION"])
            print("\n")

#查看城市位置("google_map_api)
            while True:
                c2 = input("See the location of the city press \"c\",Go back press\"b\",Quit press\"q\"\n")
                if c2 == "c":
                    city = info_dict["CommonPlayerInfo"][0]["TEAM_CITY"]
                    url = "https://maps.googleapis.com/maps/api/staticmap?center=USA&zoom=4&size=1600x1600&markers="+city+"&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
                    #print(url)
                    response = requests.get(url)
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    while True:
                        try:
                            zoom = int(input("To see more specific about the city by setting zoom\n"
                                             "1: World 5: Landmass/continent 10: City 15: Streets  20: Buildings\n"
                                             "Enter a number you want to set:"))
                            url = "https://maps.googleapis.com/maps/api/staticmap?center="+city+"&zoom=" + str(
                                zoom) + "&size=800x800&markers=" + city + "&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
                            response = requests.get(url)
                            img = Image.open(BytesIO(response.content))
                            img.show()
                            c3 = input("Continue press\"c\", Go back press\"b\", Quit press\"q\"\n")
                            if c3 == "c":
                                continue
                            elif c3 == "b":
                                break
                            elif c3 == "q":
                                exit()
                            else:
                                print("Please enter qualified character!")
                                continue
                        except ValueError:
                            print("Wrong input!")
                            continue
                elif c2 == "b":
                    break
                elif c2 == "q":
                    exit()
                else:
                    print("Please enter qualified character!")
                    continue


#查找球隊(nba_api, 爬蟲)
        elif c1 == "t":
            url = "https://geojango.com/pages/list-of-nba-teams"
            html = urllib.request.urlopen(url).read()  # url存網址 html打開
            soup = BeautifulSoup(html, "html.parser")
            body_tag = soup.find("body")

            # path
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
            # key:team name, value:info
            for content in span_tag:
                i += 1
                if i % 5 == 1:
                    team_info.setdefault(content.get_text(), [])
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
                            print(arena_list[i]+information)
                            if i == 1:
                                city = information
                            i += 1
                        flag = 1
                if flag == 1:
                    break
                else:
                    print("Wrong Name!")
                    continue

            while True:
                c2 = input("See the location of the city press \"c\",Go back press\"b\",Quit press\"q\"\n")
                if c2 == "c":
                    url2 = "https://maps.googleapis.com/maps/api/staticmap?center=USA&zoom=4&size=800x800&markers="+city+"&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
                    #print(url2)
                    response = requests.get(url2)
                    img = Image.open(BytesIO(response.content))
                    img.show()
                    while True:
                        try:
                            zoom = int(input("To see more specific about the city by setting zoom\n"
                                             "1: World 5: Landmass/continent 10: City 15: Streets  20: Buildings\n"
                                             "Enter a number you want to set:"))
                            url = "https://maps.googleapis.com/maps/api/staticmap?center="+city+"&zoom=" + str(
                                zoom) + "&size=800x800&markers=" + city + "&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
                            response = requests.get(url)
                            img = Image.open(BytesIO(response.content))
                            img.show()
                            c3 = input("Continue press\"c\", Go back press\"b\", Quit press\"q\"\n")
                            if c3 == "c":
                                continue
                            elif c3 == "b":
                                break
                            elif c3 == "q":
                                exit()
                            else:
                                print("Please enter qualified character!")
                                continue
                        except ValueError:
                            print("Wrong input!")
                            continue
                elif c2 == "b":
                    break
                elif c2 == "q":
                    exit()
                else:
                    print("Please enter qualified character!")
                    continue
        else:
            print("Please enter qualified character!")
            continue
    except ValueError:
        print("Please enter qualified character!")
        continue
