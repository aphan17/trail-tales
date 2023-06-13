from django.urls import path
from posts.views import posts_list, post_detail

urlpatterns = [
    path("", posts_list, name="homepage"),
    path("<int:id>/", post_detail, name="post_detail"),
]
