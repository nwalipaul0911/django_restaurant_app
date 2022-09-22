from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.db import models

# Create your models here.
class Menu(models.Model):
  menu_categories = (
    ('breakfast', 'breakfast'),
    ('lunch', 'lunch'),
    ('dinner', 'dinner'),
    ('drinks', 'drinks'),
    ('desserts', 'desserts'),
  )
  menu_category = models.CharField(max_length=40, choices=menu_categories)
  name = models.CharField(max_length=100)
  photo = models.ImageField('menu photo', upload_to = 'menu_photo', validators=[FileExtensionValidator(['png'])])
  price = models.FloatField()
  description = models.TextField(max_length=150)

  def __str__(self):
    return self.name

class Order(models.Model):
  name = models.CharField(max_length=100)
  e_mail = models.EmailField()
  address = models.TextField(max_length=150)
  order_number = models.CharField(max_length=50)
  quantity = models.IntegerField()
  order_date = models.DateField(auto_now_add= timezone.localdate)
  order_time = models.TimeField(auto_now_add=timezone.localtime)

  def __str__(self):
    return self.name

class Table(models.Model):
  name = models.CharField(max_length=100)
  guests = models.IntegerField()
  e_mail = models.EmailField()
  booking_number = models.CharField(max_length=100)
  date_visiting = models.DateField()
  time_visiting = models.TimeField()
  booking_date = models.DateField(auto_now_add= timezone.localdate)
  booking_time = models.TimeField(auto_now_add= timezone.localtime)

  def __str__(self):
    return self.name

class Contact(models.Model):
  name = models.CharField(max_length=100)
  e_mail = models.EmailField()
  message = models.TextField(max_length=500)

  def __str__(self):
    return self.name