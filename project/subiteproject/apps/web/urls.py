"""Web urls"""

# Django
from django.urls import include, path
from django.contrib.auth.decorators import login_required

from .views.signin import SignInTemplateView
from .views.index import IndexTemplateView


urlpatterns = [
    path('signin/', SignInTemplateView.as_view(), name='signin'),
    path('index.html', login_required(IndexTemplateView.as_view()), name='index'),
]