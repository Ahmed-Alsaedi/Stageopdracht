from email.policy import default
from django.db import models

# Create your models here.
class City(models.Model):    
    cityCode = models.CharField(max_length=255) #unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Hotel(models.Model): 
    # foreign key naar city. Want elk hotel heeft precies 1 city   
    city= models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    cityCode= models.CharField(max_length=255)
    hotelNr = models.CharField(max_length=255)
    name = models.CharField(max_length=255)