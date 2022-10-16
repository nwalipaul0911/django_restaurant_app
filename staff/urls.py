from django.urls import path
from .views import *

urlpatterns = [
    path('staff_page/', home, name='staff-home'),
    path('staff_contact/<int:id>', contact_view,name='staff-contact'),
    path('staff_reservation/<int:id>', reservation_view,name='staff-reservation'),
    path('staff_menu/<int:id>', menu_view,name='staff-menu'),
    path('staff_order/<int:id>', order_view,name='staff-order'),
]