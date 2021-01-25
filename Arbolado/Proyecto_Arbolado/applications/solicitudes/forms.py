# Django Modules
from django import forms
# Django Models
from .models import SolicitudeRegister, SolicitudeReport

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
        
# SolicitudeReport Form        
class SolicitudeReportForm(forms.ModelForm):
    
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

    description = forms.CharField(
        required=True,
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Explicar detalladamente el incidente...',
                'rows': '6',
                'cols': '50',
            }
        )
    )

    address = forms.CharField(
        required=True,
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Seleciona la ubicación en el mapa...',
                'rows': '4',
                'cols': '50',
                'disabled': 'true',
            }
        )
    )    

    class Meta:
        model = SolicitudeReport
        fields = (
            'full_name',
            'email',
            'age',
            'image',
            'description',
            'address',
            'town',
            'status'
        )

