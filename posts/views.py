from django.shortcuts import render, get_object_or_404
from posts.models import Post

# Create your views here.

def posts_list(request):
    posts = Post.objects.all
    context = {
        "posts": posts,
    }
    return render(request, "posts/list.html", context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)
