from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import Niveau,Video
# Create your views here.

class NiveauDetail(DetailView):
	model = Niveau
	template_name = "niveau_detail.html"
