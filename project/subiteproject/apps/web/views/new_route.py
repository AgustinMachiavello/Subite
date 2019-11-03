# Django
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url


class NewRouteTemplateView(TemplateView):
    """Pantalla de ingreso para nuevas rutas de usuarios pasajeros"""
    template_name = 'new_route.html'

    def get(self, request, *args, **kwargs):
        args = {'STATIC_URL': get_static_url()}
        return render(request, self.template_name, args)