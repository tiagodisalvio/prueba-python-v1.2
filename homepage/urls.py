from django.urls import path
from .views import homepage, about
from django.urls import path, include

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/',about,name="about"),
]