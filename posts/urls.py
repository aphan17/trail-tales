from django.urls import path
from posts.views import posts_list, post_detail, create_post

urlpatterns = [
    path("", posts_list, name="homepage"),
    path("<int:id>/", post_detail, name="post_detail"),
    path("create/", create_post, name="create_post"),
]
