import os
from os.path import join, dirname
from dotenv import load_dotenv

env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)

API_KEY = os.environ.get("API_KEY")
WEATHER_URL = os.environ.get("WEATHER_URL")
LOCATION_URL = os.environ.get("LOCATION_URL")