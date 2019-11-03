"""Accounts urls"""

# Django
from django.urls import include, path

# Rest auth
from rest_auth.urls import LoginView


urlpatterns = [
    path('users/signin/', LoginView.as_view(), name='rest_signin'),
]