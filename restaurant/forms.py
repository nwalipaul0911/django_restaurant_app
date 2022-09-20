from .models import *
from django.forms import ModelForm

class MenuForm(ModelForm):

  class Meta():
    model = Menu
    fields = ('name', 'photo', 'price', 'description')

class OrderForm(ModelForm):

  class Meta():
    model = Order
    fields = ('name', 'quantity', 'e_mail', 'address')

class TableForm(ModelForm):

  class Meta():
    model = Table
    fields = ('name', 'guests', 'e_mail', 'date_visiting', 'time_visiting')

class ContactForm(ModelForm):

  class Meta():
    model = Contact
    fields = ('name', 'e_mail', 'message')
