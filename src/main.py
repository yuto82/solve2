from modules.weather.weather import get_weather
from modules.location.location import get_location
from modules.settings.settings import WEATHER_URL, LOCATION_URL,API_KEY

city = get_location(LOCATION_URL)

data_weather = get_weather(WEATHER_URL, API_KEY, city)
print(data_weather)