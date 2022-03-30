from django.contrib import admin

# Register your models here.
from .models import Niveau, Video, Module, FileUpload, SchoolYear, Exames, Ranking

admin.site.register(Niveau)
admin.site.register(Video)
admin.site.register(Module)
admin.site.register(FileUpload)
admin.site.register(Exames)
admin.site.register(SchoolYear)


class RankingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "mark", "niveau")


admin.site.register(Ranking, RankingAdmin)
