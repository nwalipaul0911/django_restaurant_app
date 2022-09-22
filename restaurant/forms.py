from .models import *
from django import forms

class MenuForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'name':'name'}))
  class Meta():
    model = Menu
    fields = ('name', 'photo', 'price', 'description')

class OrderForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'name':'name'}))
  e_mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail', 'name':'e_mail'}))
  quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Quantity', 'name':'quantity'}))
  address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Address', 'name':'address'}))
  
  class Meta():
    model = Order
    fields = ('name', 'quantity', 'e_mail', 'address')

class TableForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'name':'name'}))
  guests = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of guest(s)', 'name':'guests'}))
  e_mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail', 'name':'e_mail'}))
  date_visiting = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Date', 'name':'date_visiting'}))
  time_visiting = forms.TimeField(widget=forms.DateInput(attrs={'placeholder':'Time','name':'time_visiting'}))
  class Meta():
    model = Table
    fields = ('name', 'guests', 'e_mail', 'date_visiting', 'time_visiting')

class ContactForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'name':'name'}))
  e_mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail', 'name':'e_mail'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message', 'name':'message'}))
  class Meta():
    model = Contact
    fields = ('name', 'e_mail', 'message')
