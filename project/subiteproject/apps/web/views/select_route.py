# Django
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url

# Requests
import requests

# Route model
from subiteproject.apps.accounts.models.vehiculo import Ruta

# Urllib
import urllib.parse

# Maps utils
from subiteproject.apps.maps.views.openstreet import get_address_by_coordinates, get_cordinates_by_address
from subiteproject.apps.maps.views.route_matching import match_routes
from subiteproject.apps.maps.views.openroute import get_route_coordinates

# ALPHABET
from .preview_route import ALPHABET


class SelectRouteTemplateView(TemplateView):
    template_name = 'select_route.html'


    def get_route_addresses(self, utf8_format=False):
        """Devuelve las direcciones y las decodifica si utf8_format es Verdadero"""
        route_addresses = []
        for i in range(0, len(ALPHABET), 2):
            start_arg = self.request.GET.get(ALPHABET[i], None)
            if start_arg == None:
                break
            if not utf8_format:
                start_address = urllib.parse.unquote(start_arg)
            else:
                start_address = urllib.parse.quote(start_arg)
            end_arg = self.request.GET.get(ALPHABET[i+1], None)
            if end_arg == None:
                return None
            if not utf8_format:
                end_address = urllib.parse.unquote(end_arg)
            else:
                end_address = urllib.parse.quote(end_arg)
            route_addresses.append([start_address, end_address])
        return route_addresses

    def get(self, request, *args, **kwargs):
        """Obtiene los datos a partir de la API y meustra el trayecto en pantalla"""
        user_route_address = self.get_route_addresses()
        diff = float(self.request.GET.get('diff', 0.006)) # defualt to 300 meters
        user_route_coo_from = get_cordinates_by_address(user_route_address[0][0])
        user_route_coo_to = get_cordinates_by_address(user_route_address[0][1])
        user_route = get_route_coordinates(
            user_route_coo_from[0],
            user_route_coo_from[1],
            user_route_coo_to[0],
            user_route_coo_to[1],
        )
        matching_routes = Ruta.objects.filter(
            DestinoLat__lte=(float(user_route_coo_to[0])+diff),
            DestinoLat__gte=(float(user_route_coo_to[0])-diff),
            DestinoLon__lte=(float(user_route_coo_to[1])+diff),
            DestinoLon__gte=(float(user_route_coo_to[1])-diff),
        )
        user_route_address = self.get_route_addresses(utf8_format=True)
        driver_route_address = []
        for route in matching_routes:
            start_address = get_address_by_coordinates(route.OrigenLat, route.OrigenLon)
            end_address = get_address_by_coordinates(route.DestinoLat, route.DestinoLon)
            matching_point = match_routes(user_route, get_route_coordinates(
                route.OrigenLat, 
                route.OrigenLon, 
                route.DestinoLat, 
                route.DestinoLon), first_only=True)
            matching_address = get_address_by_coordinates(matching_point[0][1], matching_point[0][0])
            driver_route_address.append([
                route, 
                [urllib.parse.quote(start_address), urllib.parse.quote(end_address)],
                matching_address,
                ])
        args = {
            'STATIC_URL': get_static_url(), 
            'user_address': user_route_address,
            'driver_address': driver_route_address,
            }
        return render(request, self.template_name, args)