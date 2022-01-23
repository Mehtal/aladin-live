from django.shortcuts import render
from .models import Broadcast
# Create your views here.
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GetBroadcastForm
from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404
from librarry.models import Niveau


def home(request):
    # form = GetBroadcastForm()
    # if request.method == 'POST':
    #     form = GetBroadcastForm(request.POST or None)
    #     if form.is_valid():
    #         code = form.cleaned_data.get('code', None)
    #         print("--------------> code", code)

    #         try:
    #             print("--------------> try")
    #             obj = get_object_or_404(Broadcast, code=code)
    #             print("--------------> after tryyy")

    #             return redirect(obj.get_absolute_url())
    #         except Http404:
    #             print("--------------> inside exception")
    #             messages.error(
    #                 request, f"{code} n'est pas un code étudiant valide vérifiez votre sms ou contactez-nous pour un code valide")
    #             return redirect("home")
    object_list = Niveau.objects.all()

    return render(request, "home.html", {"object_list": object_list})


class BroadcastDetail(DetailView):
    model = Broadcast
    template_name = 'broadcast_detail.html'
    slug_url_kwarg = "title"


def broadcast_detail(request, id, code):
    obj = get_object_or_404(Broadcast, id=id, code=code)
    return render(request, "broadcast_detail.html", {"object": obj})
