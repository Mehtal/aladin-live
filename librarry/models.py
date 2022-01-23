from django.db import models

# Create your models here.


class Niveau(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Video(models.Model):
    niveau = models.ForeignKey(
        Niveau, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
