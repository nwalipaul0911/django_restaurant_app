from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def home(request):
  return render(request, 'restaurant/index.html')

def menu(request):
  return render(request, 'restaurant/menu.html')

def about(request):
  return render(request, 'restaurant/about.html')

def gallery(request):
  return render(request, 'restaurant/gallery.html')

def contact(request):
  return render(request, 'restaurant/contact.html')