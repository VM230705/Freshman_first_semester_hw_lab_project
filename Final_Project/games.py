import requests

url = "https://api-nba-v1.p.rapidapi.com/games/seasonYear/2019"

headers = {
    'x-rapidapi-key': "67acc2341cmsh27e9be047d07e68p127136jsn4b5a788ebb68",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)