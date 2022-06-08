from typing import Union
from settings.configuration import router

@router.get("/music/")
async def read_item(city: Union[str,None] = None, lat: Union[str,None] = None, lon: Union[str,None]= None):
    
    return {
        "city": city,
        "latitud": lat,
        "longitud": lon
    }

import requests
from typing import Union, List, Dict


class TemperatureAPI:

    def __init__(self) -> None:
        self.weather_units = 'metric'
        self.weather_url = 'http://api.openweathermap.org/data/2.5/weather'

    def _get_temperature_by_city(self, city: str) -> float:

        params: Dict = {
            'q': city
        }
        response_json: Dict = self._request_get(params)
        temperature: float = float(response_json.get('main', {}).get('temp', 30.0))
        return temperature

    def _get_temperature_by_coordinates(self, lat: float, lon: float) -> float:
        params: Dict = {
            'lat': lat,
            'lon': lon,
        }
        response_json: Dict = self._request_get(params)
        temperature: float = float(response_json.get('main', {}).get('temp', 30.0))
        return temperature

    def get_type_of_track_by_temperature(
        self,
        city: Union[str, None] = None,
        lat: Union[float, None] = None,
        lon: Union[float, None] = None,
    ) -> str:
        temperature: float = 30.0
        
        if city:
            temperature = self._get_temperature_by_city(city)
        elif lat and lon:
            temperature = self._get_temperature_by_coordinates(lat, lon)
        return 'party'

    def _request_get(self, params: Dict) -> Dict:

        response_json: Dict = {}

        url: str = f'{self.weather_url}?units={self.weather_units}'
        response = requests.get(url, params)

        if response.status_code == 200:
            response_json = response.json()

        return response_json

class TrackRecommendationAPI:
    """Class to Spotify API"""

    def __init__(self) -> None:
        self.spotify_token = 'BQBw4kkEW0-MMKEegvXk_5aXH9c-n8yOwq4k9auHOb0sPVf0VEWBcrliK1fZGBGPeqXNXjX8StjvdlaLnXwc5j0qsq42JplozymbpZEENxzLl7fVDbFqVcNc0RHl5gnf8PEQ9rxpVigt3UP25B24rY-zlPih87CPreGwWyk'
        self.spotify_url = 'https://api.spotify.com/v1/search'
        self.spotify_headers: Dict[str, str] = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_token}',
        }

    def search_recommendation(self, track_type: str) -> List[str]:
        recommendation: List[str] = []

        return recommendation

    def _search_spotify_api(params: Dict) -> Dict:
        
        return {}
        