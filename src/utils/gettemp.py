import requests
from src.settings.settings import Configuration 

class OpenWeatherMaps_API:
    async def get_temp_by_lat_lon(self, lat, lon):
        API_key = Configuration.KEY_API_OPEN_WEATHER
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric")
        temp = data.json()["main"]["temp"]
        return temp
        
    async def get_temp_by_city(self, city):
        API_key = Configuration.KEY_API_OPEN_WEATHER
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric")
        temp = data.json()["main"]["temp"]
        return temp
