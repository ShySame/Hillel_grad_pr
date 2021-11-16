"""stockroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('shop/', include('shop.urls'))
"""
from rest_framework import permissions

from web_stock import views
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'bookinst', views.BookInstanceViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'bookauthor', views.BookAuthorViewSet)


urlpatterns = [

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
