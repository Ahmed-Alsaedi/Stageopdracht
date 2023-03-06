from audioop import reverse
from django.shortcuts import render
from .models import City, Hotel, Room, Reservation, User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.management import call_command
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ReservationForm, UserForm


def update(request):
    """Updates cities and hotels, this is normally done via Command.py as cronjob.
    Added it here to showcase it easily"""
    if request.method == 'POST':
        call_command('Command')
    return redirect('/')

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

def reservation(request, room_id, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.save()
            return redirect('confirm_reservation', room_id = room.id, hotel_id = hotel.id, reservation_id=reservation.id)
    else:
        form = ReservationForm()
    
    context = {'room': room, 'hotel': hotel, 'form': form}
    return render(request, 'import_data/reservation.html', context)

def confirm_reservation(request, room_id, hotel_id, reservation_id):
    hotel = Hotel.objects.get(id=hotel_id)
    room = Room.objects.get(id=room_id)
    reservation= Reservation.objects.get(id=reservation_id)
    price = room.price
    days = reservation.check_out - reservation.check_in
    tdays = days.days
    reservation.price = price * tdays
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.reservation = reservation
            user.save()
            # redirect or render a success page
            context = {'room_id': room.id, 'hotel_id': hotel.id, 'reservation_id': reservation.id, 'user_id': user.id}
            return success(request, context)
    else:
        form = UserForm()
    context = {'form': form, 'reservation': reservation, 'hotel':hotel, 'room': room}
    return render(request, 'import_data/confirm_reservation.html', context)

def success(request, context):
    room_id = context['room_id']
    hotel_id = context['hotel_id']
    reservation_id = context['reservation_id']
    user_id = context['user_id']
    hotel = Hotel.objects.get(id=hotel_id)
    room = Room.objects.get(id=room_id)
    reservation = Reservation.objects.get(id=reservation_id)
    user = User.objects.get(id=user_id)
    context = {'reservation': reservation, 'hotel':hotel, 'room': room, 'user':user}
    return render(request, 'import_data/success.html', context)