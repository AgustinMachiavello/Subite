# Django
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url

# Requests
import requests

# Route model
from subiteproject.apps.maps.models.route import Route


class SelectRouteTemplateView(TemplateView):
    template_name = 'select_route.html'

    def get(self, request, *args, **kwargs):
        from_name = request.GET.get('from', None)
        to_name = request.GET.get('to', None)
        from_formated = from_name.replace(' ', '%20')
        from_formated = from_formated.replace(',', '%2C')
        to_formated = to_name.replace(' ', '%20')
        to_formated = to_formated.replace(',', '%2C')
        coo_from = requests.get(url = 'https://nominatim.openstreetmap.org/search?q={0}&format=json'.format(from_formated), params = {}) 
        coo_to = requests.get(url = 'https://nominatim.openstreetmap.org/search?q={0}&format=json'.format(to_formated), params = {}) 
        data_from = coo_from.json() 
        data_to = coo_to.json() 
        end_point_to = [float(data_to[0]["lat"]), float(data_to[0]["lon"])]
        print("END POINT:", end_point_to)
        diff = 0.1
        routes = Route.objects.filter(
            end_point_lat__lte=(end_point_to[0]+diff),
            end_point_lat__gte=(end_point_to[0]-diff),
            end_point_lon__lte=(end_point_to[1]+diff),
            end_point_lon__gte=(end_point_to[1]-diff),
        )
        args = {'STATIC_URL': get_static_url(), 'ROUTES': routes}
        return render(request, self.template_name, args)