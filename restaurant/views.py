from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def home(request):
  return render(request, 'restaurant/index.html')

def menu(request):
  return render(request, 'restaurant/menu.html')

def about(request):
  return render(request, 'restaurant/about.html')

def service(request):
  return render(request, 'restaurant/service.html')

def contact(request):
  return render(request, 'restaurant/contact.html')

def table(request):
  return render(request, 'restaurant/table.html')

def order(request):
  return render(request, 'restaurant/order.html')