from django.db import models

# Create your models here.
class City(models.Model):    
    city_code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Hotel(models.Model): 
    """foreign key to city. each hotel got 1 city """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    hotel_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description=models.TextField(default="")
    photo = models.ImageField(upload_to='import_data/hotel_photos/', default="Media/coming_soon.avif")


class Room(models.Model):
    name = models.CharField(max_length=255)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='import_data/room_photos/', default="Media/coming_soon.avif")
    description=models.TextField(default="")
    price = models.IntegerField(default=0)

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    agreement = models.BooleanField(default=False)