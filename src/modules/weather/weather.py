import requests

def get_weather(url, api_key, city): 
    url = f"{url}appid={api_key}&q={city}"

    response = requests.get(url).json()
    return(response)