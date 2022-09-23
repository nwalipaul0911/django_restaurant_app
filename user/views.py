import email
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout , authenticate
# Create your views here.
def signIn(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password1']   
    user= authenticate(username=username,password=password)
    if user is not None and user.is_staff:
      if user.is_active:
        login(request, user)
        return redirect('restaurant-home')
      else:
        messages.error(request, 'User not found')
        return redirect('user-signin')
    elif user is not None and not user.is_staff:
      if user.is_active:
        login(request, user)
        return redirect('restaurant-home')
      else:
        messages.error(request, 'User not found')
        return redirect('user-signin')
    else:
      return redirect('user-signin')
  return render(request, 'user/signin.html')

def signOut(request):
  logout(request)
  return redirect('restaurant-home')

def signUp(request):
  form = UserRegistrationForm(request.POST)
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid:
      form.save()
      messages.success(request, 'Registration Successful')
      return redirect('restaurant-home')
    else:
      form = UserRegistrationForm()

  context = {
    'form': form
  }
  return render(request, 'user/signup.html', context)