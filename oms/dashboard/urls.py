from django.urls import include, path

from .views import * 


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('teacher/', teacher, name='teacher'),
    path('students/', students, name='students'),
    path('sayekh/', sayekh, name='sayekh'),
    path('stuff/', stuff, name='stuff'),
    path('history/', history, name='history'),
    path('gallery/', gallery, name='gallery'),
    path('amgallery/', amgallery, name='amgallery'),
    path('authority/', authority, name='authority'),
    path('mtmhistory/', mtmhistory, name='mtmhistory'),
    path('notice/', notice, name='notice'),
    path('rules/', rules, name='rules'),
    path('members/', members, name='members'),
    path('feedback/', feedback, name='feedback'),
    path('mullfound/', mullfound, name='mullfound'),
    path('kollanfound/', kollanfound, name='kollanfound'),
]