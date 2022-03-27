from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Niveau, Video, SchoolYear
# Create your views here.


class NiveauDetail(DetailView):
    model = Niveau
    template_name = "niveau_detail.html"


class SchoolYearDetail(DetailView):
    model = SchoolYear
    template_name = "year_detail.html"
