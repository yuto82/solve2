from modules.weather.weather import get_weather
from modules.settings.settings import BASE_URL, API_KEY

city = "Warsaw"

data_weather = get_weather(BASE_URL, API_KEY, city)
print(data_weather)