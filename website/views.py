from django.shortcuts import render
from . import models
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email

def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False



def index(request):
    banners = models.Banner.objects.filter(status=True)
    protects = models.Protect.objects.filter(status=True)
    about = models.About.objects.filter(status=True).first()
    doctor = models.Doctor.objects.filter(status=True).first()
    news = models.News.objects.filter(status=True)
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

@csrf_exempt
def postmail(request):
    success, message = False, " "
    if request.method =="POST":
        email = json.loads(request.POST.get("email"))
        if  not email.isspace:
            message = 'remplir les champs'
        elif not is_email(email):
            message = 'invalide'
        else:
            newsletter = models.Newsletter(email=email)
            newsletter.save()
            success = True
            message = 'validé'

    datas = {
        'success': success,
        'message': message
    }
    return JsonResponse(datas, safe=False)
