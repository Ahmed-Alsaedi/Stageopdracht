from django import forms
from .models import City

class CitySelectForm(forms.Form):

    city = forms.ModelChoiceField(queryset=City.objects.all())