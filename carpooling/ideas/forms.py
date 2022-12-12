from django import forms
from .models import User, Ride, City

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'passwd']
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