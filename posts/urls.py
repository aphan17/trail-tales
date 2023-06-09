from django.urls import path
from posts.views import posts_list


urlpatterns = [
    path("", posts_list, name="homepage"),
]
