from django.db import models
from djanjo.conf import settings

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=10, decimal_places=1)
    elevation = models.IntegerField(max_length = 10000)
    description = models.TextField(max_length=2000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.author
