from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Niveau, Video, SchoolYear, Ranking
# Create your views here.


class NiveauDetail(DetailView):
    model = Niveau
    template_name = "niveau_detail.html"


class SchoolYearDetail(DetailView):
    model = SchoolYear
    template_name = "year_detail.html"


class RankingListView(ListView):
    model = Ranking
    template_name = "best_grades.html"
    ordering = ("niveau", "mark")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["primary"] = Ranking.objects.filter(niveau__lte=6)
        context["leng"] = Ranking.objects.filter(niveau__lte=6).count()
        context["college"] = Ranking.objects.filter(
            niveau__lte=10, niveau__gte=7)
       
        context["high"] = Ranking.objects.filter(
            niveau__lte=13, niveau__gte=11)
        return context
