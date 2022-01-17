from nba_api.stats.static import teams,players
#from nba_api.stats.endpoints import commonplayerinfo
team_dict = teams.get_teams()
player_dict = players.get_active_players()
#player = [player for player in player_dict if player["full_name"] == "LeBron James"]
#team = [team for team in team_dict if team["full_name"] == "Boston Celtics"]
#print(player_dict)
#team_id = team[0]["id"]
#print(team_id)
#player_id = player[0]["id"]
#print(player)
print(team_dict)


from nba_api.stats.endpoints import commonplayerinfo
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
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
# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, headers=custom_headers, timeout=200)
print(player_info)
