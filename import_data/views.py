from django.shortcuts import render
from .forms import CitySelectForm
from .models import Hotel

def city_select_view(request):
    if request.method == 'POST':
        form = CitySelectForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            hotels = Hotel.objects.filter(city=city)
            return render(request, 'template/import_data/hotel_list.html', {'hotels': hotels, 'city': city})
    else:
        form = CitySelectForm()
    return render(request, 'template/import_data/city_select.html', {'form': form})