from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
  list_display = ('id', 'price', 'name', 'description')
  list_display_links = ('id', 'name')
  list_filter = ('price', 'name')
  search_fields = ('name', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'address', 'order_number')
  list_display_links = ('id', 'name')
  list_filter = ('order_date',)
  search_fields = ('order_date',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
  list_display = ('id', 'date_visiting', 'name', 'booking_number')
  list_display_links = ('id', 'name')
  list_filter = ('date_visiting',)
  search_fields = ('date_visiting',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'message')
  list_display_links = ('id', 'title')