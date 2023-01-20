from django.contrib import admin
from .models import Hotel
from .models import City

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    """Used for displaying / ordering / editing the hotel at the admin page at /admin"""
    list_display = ('city', 'cityCode','hotelNr','name')
    ordering = ('city','name',)
    search_fields = ('city','cityCode','hotelNr','name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Used for displaying / ordering / editing the cities at the admin page at /admin"""
    list_display = ('name', 'cityCode')
    ordering = ('name',)
    search_fields = ['name', 'cityCode']
