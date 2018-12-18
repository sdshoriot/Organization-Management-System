from django.urls import include, path
from home.views import *


urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('feedback/', feedback, name='feedback'),
]