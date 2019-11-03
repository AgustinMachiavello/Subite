"""subiteproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Accounts app
    path('api/', include(('subiteproject.apps.accounts.urls', 'users'), namespace='users')),
    # Web app
    path('', include(('subiteproject.apps.web.urls', 'web'), namespace='web')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
