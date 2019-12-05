from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='defaul.jpg', upload_to='profile_pictures')

    objects = models.Manager

    def __str__(self):
        return f'{self.user.username}'

