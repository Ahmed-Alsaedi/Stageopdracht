from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.select_city),
    path('get_hotels/', views.get_hotels, name='get_hotels'),
    path('update/', views.update, name='run_command'),
]