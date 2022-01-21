from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Broadcast(models.Model):
    title = models.CharField(max_length=20, default="we are live")
    code = models.CharField(max_length=10, unique=True)
    is_live = models.BooleanField(default=False)
    video = models.CharField(max_length=100, default="")
    created = models.DateField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('broadcast-detail', args=[self.id, self.code])

    def __str__(self):
        return f'{self.title} {self.code}'
