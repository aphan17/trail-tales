from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date",
        "author",
        "id",
    )
    search_fields = ['name']
