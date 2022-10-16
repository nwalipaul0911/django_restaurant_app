from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='restaurant-home'),
    path('menu/', menu, name='restaurant-menu'),
    path('about/', about, name='restaurant-about'),
    path('contact/', contact, name='restaurant-contact'),
    path('order/<int:id>', order, name='restaurant-order'),
    path('table/', table, name='restaurant-table'),
    path('search/', search, name='restaurant-search'),
    path('user/', user_view, name='restaurant-user'),
]