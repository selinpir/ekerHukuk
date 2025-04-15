from django.http import HttpResponse
from django.urls import path
from . import views
from ekerHukuk import admin


def home(request):
    return HttpResponse('anasayfa') #ctrl . ile kutuphaneye eklenir

def hakkimizda(request):
    return HttpResponse('hakkimizda') 

def hizmetler(request):
    return HttpResponse('hizmetler') 

def blog(request):
    return HttpResponse('blog') 

def iletisim(request):
    return HttpResponse('iletisim') 

urlpatterns = [
  
    path('',home),
    path('anasayfa',home),
    path('hakkimizda',hakkimizda),
    path('hizmetler',hizmetler),
    path('blog',blog),
    path('iletisim',iletisim),
    path('admin/', admin.site.urls),
]