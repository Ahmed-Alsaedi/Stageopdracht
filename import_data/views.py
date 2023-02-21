from audioop import reverse
from django.shortcuts import render
from .models import City, Hotel, Room
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.management import call_command
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def update(request):
#     """Updates cities and hotels, this is normally done via Command.py as cronjob.
#     Added it here to showcase it easily"""
#     if request.method == 'POST':
#         call_command('Command')
#     return redirect('/')




def hotel_list(request):
    # Retrieve the selected city name from the query parameter
    selected_city_name = request.GET.get('city')

    # Filter the Hotel model to retrieve all hotels in the selected city
    hotels = Hotel.objects.filter(city__name=selected_city_name)

    # Create a Paginator object with 6 hotels per page
    paginator = Paginator(hotels, 6)

    # Retrieve the current page number from the query parameter
    page_number = request.GET.get('page')

    # Retrieve the current page object from the Paginator object
    page_obj = paginator.get_page(page_number)

    # Render a template that displays the list of hotels
    return render(request, 'import_data/hotel_list.html', {'hotels': page_obj, 'selected_city_name': selected_city_name})






def select_city(request):
    if request.method == 'POST':
        # Get the selected city code from the form data
        selected_city_code = request.POST.get('city_code')

        # Retrieve the hotels in the selected city
        hotels = Hotel.objects.filter(city__cityCode=selected_city_code)

        # Render the hotel list page with the hotels and selected city
        return render(request, 'import_data/hotel_list.html', {'hotels': hotels, 'selected_city_code': selected_city_code})

    # If the request method is not POST, render the city selection page
    cities = City.objects.all()
    return render(request, 'import_data/city_select.html', {'cities': cities})

def room_list(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    context = {'hotel': hotel, 'rooms': rooms}
    return render(request, 'import_data/room_list.html', context)








# def get_hotels(request):
#     """Returns json data of the corresponding hotels for a city"""
#     city_id = request.GET.get('city_id')
#     hotels = Hotel.objects.filter(city=city_id)
#     data = {'hotels': list(hotels.values())}
#     return JsonResponse(data)

# def rooms_view(request):
#     return render(request, 'import_data/rooms.html')