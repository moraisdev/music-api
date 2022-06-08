from fastapi import APIRouter, FastAPI
from pydantic import BaseSettings

app = FastAPI()
router = APIRouter()

class ConfigurationEnv(BaseSettings):
    KEY_API_OPEN_WEATHER: str = "KEY_API_OPEN_WEATHER"
