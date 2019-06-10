from django.urls import include, path
from home.views import *


urlpatterns = [
    path('', home, name='home'),
    path('message-detail/<int:pk>', message_detail, name='message_detail'),
    path('gallery/', gallery, name='gallery'),
    path('feedback/', feedback, name='feedback'),
]