from django.contrib import admin

# Register your models here.
from .models import Niveau, Video

admin.site.register(Niveau)
admin.site.register(Video)
