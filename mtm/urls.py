from django.urls import include, path
from .views import * 


urlpatterns = [
    path('authority/', authority, name='authority'),
    path('authority-detail/<int:pk>', authority_detail, name='authority-detail'),
    path('member/', member, name='member'),
    path('vission/', vission, name='vission'),
    path('second/', second, name='second'),
    path('award/', award, name='award'),
    path('rules/', rule, name='rules'),
    path('mtmhistory/', mtmhistory, name='mtmhistory'),
]