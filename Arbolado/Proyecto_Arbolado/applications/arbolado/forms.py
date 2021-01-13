# Django Modules
from django import forms
# Django Models
from .models import Section, Species, Town, Tree

# Section Form
class SectionForm(forms.ModelForm):
    """Form definition for Section""" 

    town = forms.ModelChoiceField(
        required = True,
        queryset = Town.objects.all(),
        empty_label = "Selecciona una...",
    ) # ChoiceField bonded to Town model
    
    # The fields that are not specified in this section won´t be registered in the Database
    class Meta:
        model = Section
        fields = (
            'trees',
            'location_name',
            'location_type',
            'address',
            'town'
        )

class TreeForm(forms.ModelForm):
    """Form definition for Tree"""
    
    species = forms.ModelChoiceField(
        required = True,
        queryset = Species.objects.all(),
        empty_label = "Selecciona una...",
    ) # ChoiceField bonded to Species model

    description = forms.CharField(
        required=True,
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Tamaño, altura, características...',
                'rows': '4',
                'cols': '50',
            }
        )
    )

    amount = forms.IntegerField(
        required = True,
        min_value = 1,
        widget = forms.NumberInput(
            attrs={
                'value': '1'
            }
        )
    ) 

    class Meta:
        model = Tree
        # Or fields = ('__all__')
        fields = (
            'species',
            'description',
            'image',
            'status',
            'amount'       
        )

