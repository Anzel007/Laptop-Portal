from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'brand', 'price', 'processor', 'ram', 'storage', 'image']
