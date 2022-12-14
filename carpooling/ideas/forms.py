from django import forms
from .models import User, Ride, City
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'phone_number', 'passwd']
        phone_number = PhoneNumberField()
        widgets = {
            'passwd': forms.PasswordInput(),
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