# Requests
import requests

# Parse
import urllib.parse


def get_cordinates_by_address(address :str):
    """Returns latitude and longitude of a given address
    
    More info at: https://nominatim.openstreetmap.org/search?q=ituzaingo%201395%2Csalto%2Curuguay
    """
    utf8_address = urllib.parse.quote(address)
    url = 'https://nominatim.openstreetmap.org/search?q={0}&format=json'.format(utf8_address)
    data = requests.post(url).json()
    return [data[0]["lat"], data[0]["lon"]]


def get_address_by_coordinates(lat :float, lon :float):
    """Returns the address of a given coordinate
    
    More info at: https://nominatim.openstreetmap.org/reverse.php?lat=-31.40410&lon=-57.95156&zoom=18&format=html
    """
    url = 'https://nominatim.openstreetmap.org/reverse?lat={0}&lon={1}&format=json'.format(lat, lon)
    data = requests.post(url).json()
    print(url)
    return data["display_name"]
