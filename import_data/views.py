from audioop import reverse
from django.shortcuts import render
from .models import City, Hotel
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.management import call_command


def update(request):
    """Updates cities and hotels, this is normally done via Command.py as cronjob.
    Added it here to showcase it easily"""
    if request.method == 'POST':
        call_command('Command')
    return redirect('/')


def select_city(request):
    """'index' page, where a user can select a city from the dropdown box"""
    cities = City.objects.all()
    return render(request, 'import_data/city_select.html', {'cities': cities})


def get_hotels(request):
    """Returns json data of the corresponding hotels for a city"""
    city_id = request.GET.get('city_id')
    hotels = Hotel.objects.filter(city=city_id)
    data = {'hotels': list(hotels.values())}
    return JsonResponse(data)