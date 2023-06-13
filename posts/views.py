from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from posts.forms import PostForm

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


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.author = request.user
            post.save()
            return redirect("homepage")

    else:
        form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "posts/create.html", context)
