from django.urls import path
from .views import contact, postview

urlpatterns = [
    path("contact/", contact, name="contact"),
    path("posts/", postview, name="posts"),
]
