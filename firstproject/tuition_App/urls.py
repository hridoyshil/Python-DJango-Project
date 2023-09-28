from django.urls import path
from .views import postview, postcreate, subview, ContactView


urlpatterns = [
    # path("contact/", contact, name="contact"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("posts/", postview, name="posts"),
    path("create/", postcreate, name="create"),
    path("subjects/", subview, name="subjects"),
]
