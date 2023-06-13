from django.forms import ModelForm
from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "name",
            "hike_length",
            "elevation",
            "description",
            "date",
            "author",
        ]
