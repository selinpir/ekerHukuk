from django.shortcuts import render

def anasayfa(request):
    return render(request,"anasayfa.html")

def hakkimizda(request):
    return render(request,"hakkimizda.html")

def hizmetler(request):
    return render(request,"hizmetler.html")

def blog(request):
    return render(request,"blog.html")

def iletisim(request):
    return render(request,"iletisim.html")

#SSS-faq
from .models import SSS
def anasayfa(request):
    faqs = SSS.objects.all()
    return render(request, 'anasayfa.html', {'faqs': faqs})

#hakkimizda
from .models import AvukatOzgecmis, VizyonMisyon, BasindaBiz
def hakkimizda(request):
    context = {
        'avukatlar': AvukatOzgecmis.objects.all(),
        'vizyon_misyon': VizyonMisyon.objects.first(),
        'basinda_biz': BasindaBiz.objects.all(),
    }
    return render(request, 'hakkimizda.html', context)