from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

#http://127.0.0.1:8000/ --> anasayfa
#http://127.0.0.1:8000/home -->anasayfa
#http://127.0.0.1:8000/kanunlar --> kanunlar

'''
anasayfa
hakkımızda 
hizmetler/uzmanlık alanları
blog/makaleler
iletişim sayfası
danışmanlık ??
'''

urlpatterns = [
    path( include('anasayfa.urls')),
    path( include('hakkimizda.urls')),
    path( include('hizmetler.urls')),
    path( include('blog.urls')),
    path( include('iletisim.urls')),
    path( include('admin.urls')),
    path('admin/', admin.site.urls),
]
