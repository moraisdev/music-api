from src.settings import KEY_API_OPEN_WEATHER, router

router.post("/city-coords")
def get_temp_from_lat_long():
    url = f"http://api.openweathermap.org/data/2.5/weather?{lat}&{long}&appid={KEY_API_OPEN_WEATHER}"


router.post("/city-name")
def get_temp_from_city():
    return "get_playlist"
