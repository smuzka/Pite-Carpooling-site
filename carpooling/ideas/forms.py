from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Ride, City
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'about_me', 'birth_date', 'profile_picture', 'email', 'phone_number', 'password']
        phone_number = PhoneNumberField()
        birth_date = forms.DateField()
        widgets = {
            'password': forms.PasswordInput(),
        }



class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['price', 'seats_left', 'allow_pets', 'leave_date', 'arrival_date', 'begin_city', 'end_city']
        begin_city = forms.ModelChoiceField(
            queryset=City.objects.all(),
            required=True,
        )
        end_city = forms.ModelChoiceField(
            queryset=City.objects.all(),
            required=True,
        )