from django.db import models

# Create your models here.
class City(models.Model):    
    cityCode = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Hotel(models.Model): 
    """foreign key to city. each hotel got 1 city """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    cityCode= models.CharField(max_length=255)
    hotelNr = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    #img = models.ImageField(upload_to='room_images/')
