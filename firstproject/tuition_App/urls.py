from django.urls import path
from .pdf import contact_pdf

from .views import (
    subview,
    ContactView,
    PostCreareView,
    PostListView,
    postview,
    PostDetailView,
    PostEditView,
    PostDeleteView,
    contact,
    search,
    filter,
    postview,
    likepost,
    addcomment,
    addphoto,
    postcreate,
)

# from .views import  postcreate,contact,

app_name = "tuition_App"

urlpatterns = [
    # path("contact/", contact, name="contact"),
    path("create/", postcreate, name="create"),
    path("search/", search, name="search"),
    path("filter/", filter, name="filter"),
    path("pdf/", contact_pdf, name="pdf"),
    path("addcomment/", addcomment, name="addcomment"),
    path("likepost/<int:id>/", likepost, name="likepost"),
    # path("postview/", postview, name="postview"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("posts/", postview, name="posts"),
    path("addphoto/<int:id>/", addphoto, name="addphoto"),
    path("postlist/", PostListView.as_view(), name="postlist"),
    path("postdetail/<int:pk>/", PostDetailView.as_view(), name="postdetail"),
    path("edit/<int:pk>/", PostEditView.as_view(), name="edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
    path("subjects/", subview, name="subjects"),
    # path("create/", PostCreareView.as_view(), name="create"),
]
