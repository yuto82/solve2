import requests
from modules.location.location import get_location
from modules.settings.settings import WEATHER_URL, API_KEY


def get_weather(city=None): 
    if city is None:
        city = get_location()

    url = f"{WEATHER_URL}appid={API_KEY}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_feels_like = data['main']['feels_like']
        celsius = int(kelvin_to_celsius(temp_kelvin))
        temp_feels = int(kelvin_to_celsius(temp_feels_like))
        return(celsius, temp_feels)
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching weather data: {e}")
        return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15




