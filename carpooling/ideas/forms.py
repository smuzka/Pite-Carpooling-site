from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'passwd']
        widgets = {
            'passwd': forms.PasswordInput(),
        }