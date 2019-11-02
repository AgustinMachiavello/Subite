# Django
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url

# Map utils
from subiteproject.apps.maps.views import openroute, openstreet, route_matching

# Parse
import urllib.parse

# Route matching
from subiteproject.apps.maps.views.route_matching import match_routes


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class PreviewRouteTemplateView(TemplateView):
    template_name = 'preview_route.html'

    def get_route_addresses(self):
        route_addresses = []
        for i in range(0, len(ALPHABET), 2):
            start_arg = self.request.GET.get(ALPHABET[i], None)
            if start_arg == None:
                break
            start_address = urllib.parse.unquote(start_arg)
            end_arg = self.request.GET.get(ALPHABET[i+1], None)
            if end_arg == None:
                return None
            end_address = urllib.parse.unquote(end_arg)
            route_addresses.append([start_address, end_address])
        return route_addresses

    def get(self, request, *args, **kwargs):
        profile = self.request.GET.get('profile', 'driving-car')
        route_addresses = self.get_route_addresses()
        route_coordinates = []
        for i in range(len(route_addresses)):
            start_coo = openstreet.get_cordinates_by_address(route_addresses[i][0])
            end_coo = openstreet.get_cordinates_by_address(route_addresses[i][1])
            coo = openroute.get_route_coordinates(
                start_coo[0],
                start_coo[1],
                end_coo[0],
                end_coo[1],
                profile,
            )
            route_coordinates.append(coo)
        if len(route_addresses) >= 2:
            icons_coordinates = match_routes(route_coordinates[0], route_coordinates[1], first_only=True)
        else:  
            icons_coordinates = self.request.GET.get('icons', [])
        center_coordinates = self.request.GET.get('center', route_coordinates[0][0])
        args = {
            'STATIC_URL': get_static_url(),
            'center_coordinates': center_coordinates,
            'route_coordinates': route_coordinates,
            'icons_coordinates': icons_coordinates,
            }
        print("ICONS:", icons_coordinates)
        return render(request, self.template_name, args)