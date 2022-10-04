from django.shortcuts import render, redirect, get_object_or_404
from restaurant.models import *
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
  orders_today = Order.objects.all().filter(order_date =str(date.today())).order_by('order_time')
  orders = Order.objects.all().order_by('order_date')
  reservations_today = Table.objects.all().filter(date_visiting =str(date.today())).order_by('time_visiting')
  reservations = Table.objects.all().order_by('booking_date')
  menus_today = Menu.objects.all().order_by('id').filter(availability = True).order_by('menu_category')
  menus = Menu.objects.all().order_by('id').order_by('menu_category')
  contacts_today = Contact.objects.all().filter(date_sent =str(date.today())).order_by('time_sent')
  contacts = Contact.objects.all().order_by('time_sent')
  user = request.user
  context = {
    'user': user,
    'orders_today': orders_today,
    'orders': orders,
    'reservations_today': reservations_today,
    'reservations': reservations,
    'menus_today': menus_today,
    'menus': menus,
    'contacts_today': contacts_today,
    'contacts': contacts
  }
  return render(request, 'staff/staff.html', context)

def contact_view(request, id):
  contact = get_object_or_404(Contact, id=id)
  context={
    'contact': contact
  }
  return render(request, 'staff/contact.html', context)
def menu_view(request, id):
  menu = get_object_or_404(Menu, id=id)
  context={
    'menu': menu
  }
  return render(request, 'staff/menu.html', context)
def order_view(request, id):
  order = get_object_or_404(Order, id=id)
  context={
    'order': order
  }
  return render(request, 'staff/order.html', context)
def reservation_view(request, id):
  reservation = get_object_or_404(Table, id=id)
  context={
    'reservation': reservation
  }
  return render(request, 'staff/reservation.html', context)