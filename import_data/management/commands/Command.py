from django.core.management.base import BaseCommand

from django.http import HttpResponse
from import_data.models import City, Hotel
import requests
from django.http import JsonResponse
import csv



class Command(BaseCommand):
    
    def handle(self,*args, **options):
        """Handle method needs to be called handle, otherwise Command doesn't work.
        Users requests libary to authenticate itself and pass the responses to the corresponding
        methods"""
        
        city_url = "http://rachel.maykinmedia.nl/djangocase/city.csv"
        hotel_url = "http://rachel.maykinmedia.nl/djangocase/hotel.csv"
        username = "python-demo"
        password = "claw30_bumps"

        city_response = requests.get(city_url, auth=(username, password))
        hotel_response = requests.get(hotel_url, auth=(username, password))

        if city_response.status_code != 200 or hotel_response.status_code != 200: # Make sure the request was successful
            print("No 200 status code returned... exiting")
            return
        
        self.city_db_update(city_response)
        self.hotel_db_update(hotel_response)

        #return HttpResponse("Everything went correctly.")
        print("Successfully updated")



    def hotel_db_update(self,hotel_response):
        """Updates or creates the database with the information from the hotel response"""
        hotel_csv = hotel_response.content.decode() # Get the content of the CSV file
        reader = csv.reader(hotel_csv.splitlines(), delimiter=';') # split csv with ; delimiter

        columns = ["city_code", "hotel_number", "name" ] # the column names
        # Insert the data from the CSV into the table
        for row in reader:
            if len(row) == len(columns):
                city = City.objects.get(city_code=row[0])
                hotel, created = Hotel.objects.update_or_create(
                    hotel_number=row[1],
                    defaults={
                        "city": city,
                        "city_code": row[0],
                        "name": row[2]
                    }
                )
                if created:
                    print(f"Record created with values {row}")
                elif hotel.name != row[2] or hotel.city_code != row[0]:
                    print(f"Record updated with values {row}")
                else:
                    print(f"Nothing changed")
            else:
                print(f"Skipping row {row} as it has {len(row)} columns, expected {len(columns)}")


    def city_db_update(self,city_response):
        """Updates or creates the database with the information from city response"""
        city_csv = city_response.content.decode() # Get the content of the CSV file
        reader = csv.reader(city_csv.splitlines(), delimiter=';') # split csv with ; delimiter

        columns = ["city_code", "name"] # the column names
        # Insert the data from the CSV into the table
        for row in reader:
            if len(row) == len(columns):
                city, created = City.objects.update_or_create(
                    city_code=row[0],
                    defaults={
                        "name": row[1]
                    }
                )
                if created:
                    print(f"Record created with values {row}")
                elif city.name != row[1]:
                    print(f"Record updated with values {row}")
                else:
                    print(f"Nothing changed")
            else:
                print(f"Skipping row {row} as it has {len(row)} columns, expected {len(columns)}")

