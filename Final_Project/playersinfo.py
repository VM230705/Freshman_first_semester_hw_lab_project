from nba_api.stats.static import teams,players
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
        print("Wrong Name")

from nba_api.stats.endpoints import commonplayerinfo

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
print(player_info.get_normalized_dict())
info_dict = player_info.get_normalized_dict()
print("BIRTHDATE:",info_dict["CommonPlayerInfo"][0]["BIRTHDATE"])
print("SCHOOL:",info_dict["CommonPlayerInfo"][0]["SCHOOL"])
print("COUNTRY:",info_dict["CommonPlayerInfo"][0]["COUNTRY"])
print("HEIGHT:",info_dict["CommonPlayerInfo"][0]["HEIGHT"])
print("WEIGHT:",info_dict["CommonPlayerInfo"][0]["WEIGHT"])
print("SEASON_EXP:",info_dict["CommonPlayerInfo"][0]["SEASON_EXP"])
print("POSITION:",info_dict["CommonPlayerInfo"][0]["POSITION"])
print("TimeFrame:",info_dict["PlayerHeadlineStats"][0]["TimeFrame"])
print("PTS:",info_dict["PlayerHeadlineStats"][0]["PTS"])
print("AST:",info_dict["PlayerHeadlineStats"][0]["AST"])
print("REB:",info_dict["PlayerHeadlineStats"][0]["REB"],"\n")





team_name = str(info_dict["CommonPlayerInfo"][0]["TEAM_CITY"]+" "+info_dict["CommonPlayerInfo"][0]["TEAM_NAME"])
print(team_name+" Roster:")



team_dict = teams.get_teams()
player_dict = players.get_active_players()

for name in team_dict:
    if team_name == name["full_name"]:
        team_id = name["id"]


from nba_api.stats.endpoints import commonteamroster

team_roster = commonteamroster.CommonTeamRoster(team_id=team_id, season="2020")
for info in team_roster.get_normalized_dict()["CommonTeamRoster"]:
    print(info["PLAYER"]+" "+info["POSITION"])
print(info_dict["CommonPlayerInfo"][0]["TEAM_CITY"])
city = info_dict["CommonPlayerInfo"][0]["TEAM_CITY"]
print(city)
key = "AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"

from PIL import Image
import requests
from io import BytesIO

while True:
    c2 = input("See the location of the city press \"c\",Go back press\"b\",Quit press\"q\"")
    if c2 == "c":
        city = info_dict["CommonPlayerInfo"][0]["TEAM_CITY"]
        url = "https://maps.googleapis.com/maps/api/staticmap?center=USA&zoom=4&size=1600x1600&markers=" + city + "&key="+key
        print(url)
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
    elif c2 == "b":
        break
    elif c2 == "q":
        exit()
