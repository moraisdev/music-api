from pydantic import BaseModel


class CityCoords(BaseModel):
    last: float
    long: float


class CityName(BaseModel):
    name: str
