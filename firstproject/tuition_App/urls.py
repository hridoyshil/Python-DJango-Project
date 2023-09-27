from django.urls import path
from .views import contact, postview, postcreate, subview

urlpatterns = [
    path("contact/", contact, name="contact"),
    path("posts/", postview, name="posts"),
    path("create/", postcreate, name="create"),
    path("subjects/", subview, name="subjects"),
]
