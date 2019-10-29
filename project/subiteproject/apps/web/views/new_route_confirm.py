# Django
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url


class NewRouteConfirmTemplateView(TemplateView):
    template_name = 'new_route_confirm.html'

    def get(self, request, *args, **kwargs):
        args = {'STATIC_URL': get_static_url()}
        return render(request, self.template_name, args)