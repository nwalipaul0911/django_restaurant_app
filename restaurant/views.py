from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'restaurant/index.html')

def menu(request):
  return render(request, 'restaurant/menu.html')
