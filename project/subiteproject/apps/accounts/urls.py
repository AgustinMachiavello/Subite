"""Accounts urls"""

# Django
from django.urls import include, path

# Rest auth
from rest_auth.urls import LoginView


urlpatterns = [
    """Url para el ingreso de sesión de los usuarios"""
    path('users/signin/', LoginView.as_view(), name='rest_signin'),
]