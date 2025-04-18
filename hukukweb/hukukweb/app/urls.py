from django.urls import path
from . import views

urlpatterns = [
    path("", views.anasayfa, name="anasayfa"),  # http://localhost:8000/
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),  # http://localhost:8000/hakkimizda/
    path("hizmetler/", views.hizmetler, name="hizmetler"),  # http://localhost:8000/hizmetler/
    path("blog/", views.blog, name="blog"),  # http://localhost:8000/blog/
    path("iletisim/", views.iletisim, name="iletisim"),  # http://localhost:8000/iletisim/
]