import requests

def get_coords(address_to_fetch):

    url = 'https://nominatim.openstreetmap.org/search/' + address_to_fetch +'?format=json'

    response = requests.get(url).json()
    lat = response[0]["lat"]
    lon = response[0]["lon"]

    return lat, lon
