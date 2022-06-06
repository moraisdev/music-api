import os

from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


def get_env(name):
    try:
        return os.environ[name]
    except KeyError:
        raise KeyError(f"Env '{name}' not set.")


class Configuration(object):
    KEY_API_OPEN_WEATHER = get_env("KEY_API_OPEN_WEATHER")
    KEY_API_SPOTIFY = get_env("KEY_API_SPOTIFY")
    DATABASE_URL = get_env("DATABASE_URL")
