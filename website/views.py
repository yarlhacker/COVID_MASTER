from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')


def news(request):
    return render(request, 'news.html')


def protect(request):
    return render(request, 'protect.html')

# Create your views here.
