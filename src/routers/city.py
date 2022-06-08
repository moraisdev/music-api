from typing import Union
from settings.configuration import router

@router.get("/music/")
async def read_item(city: Union[str,None] = None, lat: Union[str,None] = None, lon: Union[str,None]= None):
    
    return {
        "city": city,
        "latitud": lat,
        "longitud": lon
    }

