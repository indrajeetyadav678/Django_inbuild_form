from django.urls import path
from .views import*

urlpatterns = [
    path('signup', home, name='home'),
    path('login/', register, name='register'),
]