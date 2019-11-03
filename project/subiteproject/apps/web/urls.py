"""Direcciones URL del sistema web"""

# Django
from django.urls import include, path
from django.contrib.auth.decorators import login_required

# Views
from .views import (
    signin,
    index,
    new_route,
    preview_route,
    select_route,
)


urlpatterns = [
    path('signin/', signin.SignInTemplateView.as_view(), name='signin'), # incio de sesión
    path('index.html', login_required(index.IndexTemplateView.as_view()), name='index'), # página principal
    path('new_route.html', login_required(new_route.NewRouteTemplateView.as_view()), name='new_route'), # estalbecer una nueva ruta
    path('preview_route/', login_required(preview_route.PreviewRouteTemplateView.as_view()), name='preview_route'), # previsualziar rutas
    path('select_route/', login_required(select_route.SelectRouteTemplateView.as_view()), name="select_route") # seleccionar ruta
]