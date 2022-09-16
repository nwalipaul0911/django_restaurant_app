from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='restaurant-home'),
    path('menu/', menu, name='restaurant-menu'),
]