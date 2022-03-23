from django.contrib import admin

# Register your models here.
from .models import Niveau, Video, Module, FileUpload, SchoolYear, Exames

admin.site.register(Niveau)
admin.site.register(Video)
admin.site.register(Module)
admin.site.register(FileUpload)
admin.site.register(Exames)
admin.site.register(SchoolYear)
