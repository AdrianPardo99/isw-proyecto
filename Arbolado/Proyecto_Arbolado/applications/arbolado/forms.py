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

    class Meta:
        model = Section
        fields = (
            'trees',
            'location',
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

    class Meta:
        model = Tree
        # Or fields('__all__')
        fields = (
            'name',
            'species',
            'description',
            'image',
            'status',
            'amount'       
        )

