from django.urls import path
from .views import postview, subview, ContactView, PostCreareView

# from .views import  postcreate,contact

app_name = "tuition_App"

urlpatterns = [
    # path("contact/", contact, name="contact"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("posts/", postview, name="posts"),
    path("subjects/", subview, name="subjects"),
    # path("create/", postcreate, name="create"),
    path("create/", PostCreareView.as_view(), name="create"),
]
