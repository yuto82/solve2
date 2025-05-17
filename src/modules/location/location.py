import requests

def get_location(url):
    response = requests.get(url)
    data = response.json()
    return data.get("city")