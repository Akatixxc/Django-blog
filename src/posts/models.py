from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE) #CASCADED deletes the post if user gets deleted
    image = models.ImageField(upload_to='posts_pictures')
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(default=timezone.now)

    objects = models.Manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/posts/{self.slug}/"