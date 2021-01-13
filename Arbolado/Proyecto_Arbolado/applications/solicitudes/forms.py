# Django Modules
from django import forms
# Django Models
from .models import SolicitudeRegister

# SolicitudeRegister Form
class SolicitudeRegisterForm(forms.ModelForm):

    age = forms.IntegerField(
        required = True,
        min_value = 0,
        max_value = 100,
        widget = forms.NumberInput(
            attrs={
                'value': '0'
            }
        )
    ) 

    class Meta:
        model = SolicitudeRegister
        fields = (
            'full_name',
            'email',
            'age',
            'section'
        )