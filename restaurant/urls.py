from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='restaurant-home'),
    path('menu/', menu, name='restaurant-menu'),
    path('about/', about, name='restaurant-about'),
    path('gallery/', gallery, name='restaurant-gallery'),
    path('contact/', contact, name='restaurant-contact'),
]