import json
import urllib.request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials                         #import需要的函式庫
url = urllib.request.urlopen("https://j72ajh.deta.dev/spotify_id").read()
data = json.loads(url)                                                      #url轉成json檔
print(data)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="b858d372d17b4c029f4895326a042a9a",
                                                           client_secret="b65be5a71b474d52b595da3c7e455a5b"))
track = sp.track(data["spotify_id"])                #把sp轉成json檔
artists = []
for artist in track["artists"]:                     #把所有歌手存到artists
    artists.append(artist["name"])
print("track:  ",track["name"])
print("artists:",", ".join(artists))                #用逗號個開所有歌手名稱
print("album:  ",track["album"]["name"])
print("link:   ",track["external_urls"]["spotify"])



