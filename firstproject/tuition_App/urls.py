from django.urls import path
from .views import subview, ContactView, PostCreareView, PostListView, postview

# from .views import  postcreate,contact,

app_name = "tuition_App"

urlpatterns = [
    # path("contact/", contact, name="contact"),
    # path("create/", postcreate, name="create"),
    path("posts/", postview, name="posts"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("postlist/", PostListView.as_view(), name="postlist"),
    path("subjects/", subview, name="subjects"),
    path("create/", PostCreareView.as_view(), name="create"),
]
