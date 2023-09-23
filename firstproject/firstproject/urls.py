from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home, name="home"),
    path("tuition_App/", include("tuition_App.urls")),
]
