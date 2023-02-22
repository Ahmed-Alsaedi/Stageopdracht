from django.contrib import admin
from .models import Hotel
from .models import City

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    """Used for displaying / ordering / editing the hotel at the admin page at /admin"""
    list_display = ('city', 'hotel_number','name')
    ordering = ('city','name',)
    search_fields = ('city','hotel_number','name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Used for displaying / ordering / editing the cities at the admin page at /admin"""
    list_display = ('name', 'city_code')
    ordering = ('name',)
    search_fields = ['name', 'city_code']
