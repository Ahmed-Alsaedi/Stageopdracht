from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.select_city),
    path('hotel-list/', views.hotel_list, name='hotel_list'),
    path('hotels/<int:hotel_id>/rooms/', views.room_list, name='room_list'),


    # path('get_hotels/', views.get_hotels, name='get_hotels'),
    # path('update/', views.update, name='run_command'),
    # path('rooms', views.rooms_view, name='rooms'),
]

# headers and site title for the admin portal
admin.site.site_header = "Admin portal"
admin.site.site_title = "Admin portal"
admin.site.index_title = "Welcome to the admin portal"