from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'car_make',
                  'car_model', 'license_plate', 'picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'car_make': forms.TextInput(attrs={'class': 'form-control'}),
            'car_model': forms.TextInput(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control-file'})
        }
