# Django views
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url


class ViajeSuccess(TemplateView):
	"""Pantalla web para cuando el usuario se sube a un viae exitosamente"""
	template_name = 'viaje_success.html'

	def get(self, request, *args, **kwargs):
		args = {'STATIC_URL': get_static_url()}
		return render(request, self.template_name, args)