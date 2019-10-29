"""Web urls"""

# Django
from django.urls import include, path
from django.contrib.auth.decorators import login_required

# Views
from .views import (
    signin,
    index,
    new_route,
    new_route_confirm,
)


urlpatterns = [
    path('signin/', signin.SignInTemplateView.as_view(), name='signin'),
    path('index.html', login_required(index.IndexTemplateView.as_view()), name='index'),
    path('new_route.html', login_required(new_route.NewRouteTemplateView.as_view()), name='new_route'),
    path('new_route_confirm.html', login_required(new_route_confirm.NewRouteConfirmTemplateView.as_view()), name='new_route_confirm'),
]