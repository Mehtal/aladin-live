from django.db import models
from django.urls import reverse
# Create your models here.


class Niveau(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("level-detail", kwargs={"slug": self.slug})


class Module(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Video(models.Model):
    niveau = models.ForeignKey(
        Niveau, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=50)
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, blank=True, null=True)
    link = models.CharField(max_length=150)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering: ['created']


class FileUpload(models.Model):
    niveau = models.ForeignKey(
        Niveau, on_delete=models.CASCADE, related_name="files")
    name = models.CharField(max_length=50)
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, blank=True, null=True)
    upload = models.FileField(upload_to='uploads/')
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.name}--{self.niveau}{self.module}"

    def get_absolute_url(self):
        return reverse("uploads", args[str(self.id)])


class SchoolYear(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Exames(models.Model):
    year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE,)
    niveau = models.ForeignKey(
        Niveau, on_delete=models.CASCADE, related_name="exames")
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, blank=True, null=True)
    upload = models.FileField(upload_to='uploads/exames/')
    title = models.CharField(max_length=150)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.niveau} - {self.title}'
