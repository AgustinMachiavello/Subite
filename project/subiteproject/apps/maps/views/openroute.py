"""Métodos relacionados con soliciutdes a la API de Open Route"""

# Requests
import requests


OPENROUTE_API_KEY = "5b3ce3597851110001cf6248db84a52feecd456dbb2a4ee52a35ee4f"


def get_route_coordinates(lat1, lon1, lat2, lon2, profile='driving-car'):
    """Returns a list of coordinates for the given starting and ending coordinates
    
    Main profiles options are: 'driving-car', 'foot-walking' and 'cycling-regular'

    More info at: https://openrouteservice.org/dev/#/api-docs/directions/get
    """
    url = 'https://api.openrouteservice.org/v2/directions/{0}?api_key={1}&start={2},{3}&end={4},{5}'.format(
        profile,
        OPENROUTE_API_KEY,
        lon1,
        lat1,
        lon2,
        lat2,
    )
    data = requests.get(url).json()
    return data["features"][0]["geometry"]["coordinates"]