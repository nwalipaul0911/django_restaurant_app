from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *
import random
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
  menus = Menu.objects.all().order_by('?')
  paginator = Paginator(menus, 6)
  page = request.GET.get('page')
  menus = paginator.get_page(page)
  context = {
    'menus': menus
  }
  return render(request, 'restaurant/index.html', context)

def menu(request):
  breakfasts = Menu.objects.all().filter(menu_category = 'breakfast').order_by('?')
  lunchs = Menu.objects.all().filter(menu_category = 'lunch').order_by('?')
  dinners = Menu.objects.all().filter(menu_category = 'dinner').order_by('?')
  drinks = Menu.objects.all().filter(menu_category = 'drinks').order_by('?')
  desserts = Menu.objects.all().filter(menu_category = 'desserts').order_by('?')
  context = {
    'breakfasts': breakfasts,
    'lunchs': lunchs,
    'dinners': dinners,
    'drinks': drinks,
    'desserts': desserts,
  }
  return render(request, 'restaurant/menu.html', context)

def about(request):
  return render(request, 'restaurant/about.html')

def contact(request):
  form = ContactForm(request.POST)
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      body = {
        'name': instance.name,
        'email' : instance.e_mail,
        'message': instance.message
      }
      message = '\n'.join(body.values())
      try:
        send_mail('Enquiries', message, None, ['nwalipaul353@gmail.com'],fail_silently=False)
      except BadHeaderError:
        return HttpResponse("Invalid header found.")
      messages.success(request, 'Message sent successfully.')
      return redirect('restaurant-home')
    else:
      messages.error(request, 'Please fill the contact form!')
      form = ContactForm()
  context={
    'form': form,
    'menu': menu,
  }
  return render(request, 'restaurant/contact.html', context)

def table(request):
  form = TableForm(request.POST)
  if request.method == 'POST':
    form = TableForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      random_number =random.randint(10000,500000)
      random_number2 = int((random.randint(70,90)*random_number)/7)
      instance.booking_number = random_number2
      body = {
        'name': instance.name,
        'email': instance.e_mail,
        'booking_number': f'Booking number: {instance.booking_number}',
        'guests': f'Number of guests: {instance.guests}',
        'date': f'Date: {instance.date_visiting}',
        'time': f'Time: {instance.time_visiting}'
      }
      message = '\n'.join(body.values())
      try:
        send_mail('Table Reservation', message, None,['nwalipaul353@gmail.com'],fail_silently=False )
      except BadHeaderError:
        return HttpResponse("Invalid header found.")
      messages.info(request, 'Booking Processing.')
      instance.save()
      return redirect('restaurant-home')
    else:
      messages.error(request, 'Booking not submitted. Try again')
      form = TableForm()
  context={
    'form': form,
  }
  return render(request, 'restaurant/table.html', context)

def order(request, id):
  menu = get_object_or_404(Menu, id=id)
  form = OrderForm(request.POST)
  if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      random_number = menu.id * random.randint(40000,100000)
      random_number2 = int((random.randint(10,20)*random_number)/3)
      instance.order_number = random_number2
      body = {
        'name': instance.name,
        'email': instance.e_mail,
        'order_number': f'Order number: {instance.order_number}',
        'address': f'Address: {instance.address}',
        'quantity': f'Quantity: {instance.quantity}',
      }
      message = '\n'.join(body.values())
      try:
        send_mail('New Order', message, None,['nwalipaul353@gmail.com'],fail_silently=False )
      except BadHeaderError:
        return HttpResponse("Invalid header found.")
      messages.success(request, 'Order Successful')
      instance.save()
      return redirect('restaurant-menu')
    else:
      messages.error(request, 'Booking not submitted. Try again')
      instance.save()
      return redirect('restaurant-home')
      form = OrderForm()
  context={
    'form': form,
    'menu': menu,
  }
  return render(request, 'restaurant/order.html', context)

def search(request):
  menus = Menu.objects.all().order_by('-id')
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      menus = menus.filter(name__icontains=keyword)
  context = {
    'menus': menus
  }
  return render(request, 'restaurant/search.html', context)