from django.shortcuts import render

from home.models import *


def home(request):
    return render(request, 'theme/home/home.html')   


def gallery(request):
    return render(request, 'theme/home/gallery.html')


def feedback(request):
    return render(request, 'theme/home/feedback.html')