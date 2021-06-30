from django.shortcuts import render
from . import models


def index(request):
    
    return render(request, 'index.html',locals())


def about(request):
    about = models.About.objects.filter(status=True).first()
    return render(request, 'about.html',locals())

def doctors(request):
    return render(request, 'doctors.html',locals())


def news(request):

    news = models.News.objects.filter(status=True)

    return render(request, 'news.html',locals())


def protect(request):
    protects = models.Protect.objects.filter(status=True)
    return render(request, 'protect.html',locals())

# Create your views here.
