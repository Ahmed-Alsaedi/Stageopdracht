from django import forms
from .models import Reservation, User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        if check_in and check_out:
            if check_out < check_in:
                raise forms.ValidationError('Check-out date must be after check-in date')

class UserForm(forms.ModelForm):
    agreement = forms.BooleanField(required=True, label="I agree to the terms and conditions")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address', 'country', 'zip_code', 'agreement']

class SuccessForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'email']