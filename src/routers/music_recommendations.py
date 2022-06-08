from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/get_music_recommendations/")
def read_item(city: Union[str, None] = None, lat: Union[str, None] = None, long: Union[str, None] = None):

    return {
        
    }