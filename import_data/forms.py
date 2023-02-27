from django import forms
from .models import Reservation, User, Room, Hotel

class Reservation:
    check_in = forms.DateField()
    check_out = forms.DateField()


class User:
    firs_name = forms.CharField(label='firstname', max_length=100)
    last_name = forms.CharField(label='lastname', max_length=100)
    email = forms.EmailField(label='email', max_length=254)
    address = forms.CharField(label= 'address', max_length=200)
    country = forms.CharField(label='country', max_length=100)
    zip_code = forms.CharField(label='zipcode', max_length=15)
    agreement = forms.BooleanField(default=False)