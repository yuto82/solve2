import requests
from modules.settings.settings import LOCATION_URL

def get_location(url=LOCATION_URL):
    response = requests.get(url)
    data = response.json()
    return data.get("city")