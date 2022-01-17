import json
class RegionWeather:

    _region_name = ""
    _sunday_weather_description = ""
    _minT_average = ""

    def __init__(self, region_weather):
        self.data = region_weather

    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, place):
        self._region_name = place

    @property
    def sunday_weather_description(self):
        return self._sunday_weather_description

    @sunday_weather_description.setter
    def sunday_weather_description(self, weather_description):
        self._sunday_weather_description = weather_description

    @property
    def minT_average(self):
        return self._minT_average

    @minT_average.setter
    def minT_average(self, temperature):
        self._minT_average = temperature

    def find_region_name(self):
        return self.data["locationName"]

    def find_sunday_weather(self):
        return self.data["weatherElements"]["Wx"]["daily"][1]["weather"]

    def compute_minT_avg(self):
        total,count = 0,0
        for a in self.data["weatherElements"]["MinT"]["daily"]:
            total += int(a["temperature"])
            count += 1
        return round(total/count, 2)



with open("One-week-weather.json", encoding="utf-8")as f:
    weather_data = json.load(f)
all_region_weather = weather_data["cwbdata"]["resources"]["resource"]["data"]["weatherForecasts"]["location"]

for region_weather in all_region_weather:
    get = RegionWeather(region_weather)
    get.region_name = get.find_region_name()
    get.sunday_weather_description = get.find_sunday_weather()
    get.minT_average = get.compute_minT_avg()
    print(get.region_name+"'s minT averages is", get.sunday_weather_description,", Sunday's weather is", get.minT_average)