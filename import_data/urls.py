from django.urls import path
from .views import city_select_view

urlpatterns = [
    path('city-select/', city_select_view, name='city_select'),
]