from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Create your views here.
def home(request):
  return render(request, 'restaurant/index.html')

def menu(request):
  breakfast = Menu.objects.all().filter(menu_category = 'breakfast').order_by('?')
  lunch = Menu.objects.all().filter(menu_category = 'lunch').order_by('?')
  dinner = Menu.objects.all().filter(menu_category = 'dinner').order_by('?')
  drinks = Menu.objects.all().filter(menu_category = 'drinks').order_by('?')
  desserts = Menu.objects.all().filter(menu_category = 'desserts').order_by('?')
  context = {
    'breakfast': breakfast,
    'lunch': lunch,
    'dinner': dinner,
    'drinks': drinks,
    'desserts': desserts,
  }
  return render(request, 'restaurant/menu.html', context)

def about(request):
  return render(request, 'restaurant/about.html')

def service(request):
  return render(request, 'restaurant/service.html')

def contact(request):
  form = ContactForm(request.POST)
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('restaurant-home')
  context={
    'form': form,
    'menu': menu,
  }
  return render(request, 'restaurant/contact.html')

def table(request):
  form = TableForm(request.POST)
  if request.method == 'POST':
    form = TableForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('restaurant-home')
  context={
    'form': form,
  }
  return render(request, 'restaurant/table.html')

def order(request, id):
  menu = get_object_or_404(Menu, id=id)
  form = OrderForm(request.POST)
  if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.order_number = menu.id
      instance.save()
      return redirect('restaurant-home')
  context={
    'form': form,
    'menu': menu,
  }
  return render(request, 'restaurant/order.html', context)