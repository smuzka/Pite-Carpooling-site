from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import CheckboxInput, DateTimeInput

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

        fields = ['price', 'seats_left', 'allow_pets', 'trunk', 'baby_seat', 'leave_date', 'arrival_date', 'begin_city', 'end_city']
        begin_city = forms.ModelChoiceField(
            queryset=City.objects.all(),
            required=True,
        )
        end_city = forms.ModelChoiceField(
            queryset=City.objects.all(),
            required=True,
        )
        widgets = {
            'allow_pets' : CheckboxInput(),
            'arrival_date' : DateTimeInput(),
            'leave_date' : DateTimeInput()
        }

    def __init__(self, *args, **kwargs):
        self._driver_id = kwargs.pop('driver_id')
        super(RideForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(RideForm, self).save(commit=False)
        inst.driver_id = self._driver_id
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class SearchRouteForm(forms.Form):
    origin = forms.ModelChoiceField(
            queryset=City.objects.all(),
            required=True,

        )
    destination = forms.ModelChoiceField(
        queryset=City.objects.all(),
        required=True,
    )
