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

