"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from core.routers import urlpatterns as core_api_urls
from core.urls import urlpatterns as core_urls 
from user import urls as user_urls

api_urls = core_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(api_urls)),
    path("", include(core_urls)),
    path(
        "", include((user_urls, "auth"), namespace="auth")
    ),
    path(
        "",
        TemplateView.as_view(template_name="root.html"),
        name="site_root"
    ),
]
