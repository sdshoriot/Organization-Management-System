from django.urls import include, path
from .views import * 


urlpatterns = [
	path('shaykh/', shaykh, name='shaykh'),
	path('shaykh-detail/<int:pk>', shaykh_detail, name='shaykh-detail'),
    path('teacher/', teacher, name='teacher'),
    path('teacher-detail/<int:pk>', teacher_detail, name='teacher-detail'),
    path('student/', student, name='student'),
    path('stuff/', stuff, name='stuff'),
    path('history/', history, name='history'),
]