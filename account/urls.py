from django.urls import include, path
from .views import *


urlpatterns = [
    path('sineup/', sineup, name='sineup'),
    path('login/', login, name='login'),
    path('accounts/', accounts, name='accounts'),
]