from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail'}))
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
  class Meta():
    model = User
    fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2')