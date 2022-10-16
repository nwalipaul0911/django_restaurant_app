from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *
import random
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random

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
  breakfasts = Menu.objects.all().filter(menu_category = 'breakfast').exclude(availability=False).order_by('?')
  lunchs = Menu.objects.all().filter(menu_category = 'lunch').exclude(availability=False).order_by('?')
  dinners = Menu.objects.all().filter(menu_category = 'dinner').exclude(availability=False).order_by('?')
  drinks = Menu.objects.all().filter(menu_category = 'drinks').exclude(availability=False).order_by('?')
  desserts = Menu.objects.all().filter(menu_category = 'desserts').exclude(availability=False).order_by('?')
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
      if request.user.is_authenticated:
        instance.user = request.user
      else:
        random_number =random.randint(10000,500000)
        random_number2 = int((random.randint(70,90)*random_number)/7)
        user = User(username = f'AnonymousUser{random_number2}')
        user.set_unusable_password
        user.save()
        authenticate(user=user)
        instance.user = user
      body = {
        'title': instance.title,
        'user': str(instance.user),
        'email' : instance.e_mail,
        'message': instance.message
      }
      message = '\n'.join(body.values())
      
      instance.save()
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
      if request.user.is_authenticated:
        instance.user = request.user
      else:

        user = User(username = f'AnonymousUser{random_number2}')
        user.set_unusable_password
        user.save()
        authenticate(user=user)
        instance.user = user
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
      instance.item = menu.name
      instance.status = 'processing'
      if request.user.is_authenticated:
        instance.user = request.user
      else:
        user = User(username = f'AnonymousUser{random_number2}')
        user.set_unusable_password
        user.save()
        authenticate(user=user)
        instance.user = user
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
      messages.error(request, 'Order failed. Try again')
      return redirect('restaurant-home')
      form = OrderForm()
  context={
    'form': form,
    'menu': menu,
  }
  return render(request, 'restaurant/order.html', context)

def search(request):
  menus = Menu.objects.all().filter(availability = True).order_by('-id')
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      menus = menus.filter(name__icontains=keyword)
  context = {
    'menus': menus
  }
  return render(request, 'restaurant/search.html', context)
  
@login_required
def user_view(request):
  user = request.user
  breakfasts = Menu.objects.all().filter(menu_category = 'breakfast').exclude(availability=False).order_by('?')
  lunchs = Menu.objects.all().filter(menu_category = 'lunch').exclude(availability=False).order_by('?')
  dinners = Menu.objects.all().filter(menu_category = 'dinner').exclude(availability=False).order_by('?')
  drinks = Menu.objects.all().filter(menu_category = 'drinks').exclude(availability=False).order_by('?')
  desserts = Menu.objects.all().filter(menu_category = 'desserts').exclude(availability=False).order_by('?')
  reservations = Table.objects.all().filter(user = user).order_by('-time_visiting')
  reservations_count = Table.objects.all().filter(user = user).count()
  order_list = Order.objects.all().filter(user = user).order_by('-order_time')
  order_count = Order.objects.all().filter(user = user).count()
  context = {
    'user': user,
    'breakfasts': breakfasts,
    'lunchs': lunchs,
    'dinners': dinners,
    'drinks': drinks,
    'desserts': desserts,
    'reservations': reservations,
    'reservations_count': reservations_count,
    'order_count': order_count,
    'order_list': order_list,

  }
  return render(request, 'restaurant/user.html', context)
