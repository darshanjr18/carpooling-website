from django import forms
from .models import Route
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['departure_location', 'arrival_location', 'departure_time', 'arrival_time']
        widgets = {
            'departure_location': forms.TextInput(attrs={'placeholder': 'Departure Location'}),
            'arrival_location': forms.TextInput(attrs={'placeholder': 'Arrival Location'}),
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'start_location', 'end_location', 'distance', 'arrival_time', 'arrival_location', 'departure_time', 'departure_location']