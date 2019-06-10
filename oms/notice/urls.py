from django.urls import include, path
from notice.views import notice, notice_details


urlpatterns = [
    path('notice-list/', notice, name='notice'),
    path('notice-details/<int:pk>', notice_details, name='notice-details'),
]