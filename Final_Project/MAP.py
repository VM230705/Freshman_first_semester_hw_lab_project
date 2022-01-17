import requests
import json
from bs4 import BeautifulSoup
key = "AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"

url = "https://maps.googleapis.com/maps/api/staticmap?center=USA&zoom=4&size=1600x1600&markers=Dallas&key=AIzaSyBUE1jxwZaIyaJldfRhAeoYHUwAN7e2frQ"
from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()