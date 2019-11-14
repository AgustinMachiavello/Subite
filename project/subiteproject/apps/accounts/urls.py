"""Accounts urls"""

# Django
from django.urls import include, path

# Rest auth
from rest_auth.urls import LoginView

# Viewset
from .views.users import UsuariosViewSet, ViajesViewSet

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Router Signup
routerUsuarios = DefaultRouter()
routerUsuarios.register(r'test', UsuariosViewSet, base_name='test')

# Router Signup
routerViajes = DefaultRouter()
routerViajes.register(r'viajes', ViajesViewSet, base_name='viajes')

"""Url para el ingreso de sesión de los usuarios"""
urlpatterns = [
    path('users/signin/', LoginView.as_view(), name='rest_signin'),
    path('', include(routerUsuarios.urls), name='signup'),
    path('', include(routerViajes.urls), name='viajes'),
]