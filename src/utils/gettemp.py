import requests
from settings.configuration import ConfigurationEnv 

class OpenWeatherMapsAPI:
    async def get_temp_by_lat_lon(self, lat, lon):
        api_key = ConfigurationEnv.KEY_API_OPEN_WEATHER
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
        temp = data.json()["main"]["temp"]
        return temp
        
    async def get_temp_by_city(self, city):
        api_key = ConfigurationEnv.KEY_API_OPEN_WEATHER
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
        temp = data.json()["main"]["temp"]
        return temp
