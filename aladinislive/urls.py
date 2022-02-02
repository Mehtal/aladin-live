"""aladinislive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, broadcast_detail
from librarry.views import NiveauDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('broadcast/<int:id><str:code>',
         broadcast_detail, name="broadcast-detail"),
    path('<slug:slug>', NiveauDetail.as_view(), name="level-detail"),
    path('', home, name="home"),

]
