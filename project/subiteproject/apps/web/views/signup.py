# Django views
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url


class SignUpTemplateView(TemplateView):
	"""Pantalla web para el registro de usuario"""
	template_name = 'signup.html'

	def get(self, request, *args, **kwargs):
		args = {'STATIC_URL': get_static_url()}
		return render(request, self.template_name, args)