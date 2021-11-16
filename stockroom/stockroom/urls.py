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
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi

from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Stockroom",
    ),
    patterns=[path('v1/', include('web_stock.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html',
                                             extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('v1/', include('web_stock.urls')),
    path('admin/', admin.site.urls),
]
