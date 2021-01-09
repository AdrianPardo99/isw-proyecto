from django.shortcuts import render
# Importamos nuestros modelos locales
from .models import Home

# Create your views here.
from django.views.generic import (
    TemplateView, 
)

class HomePageView(TemplateView):
    """ TemplateView Home """
    template_name = "home/index.html"
    
    # Sending all the data of the DB to HTML template
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["home"] = Home.objects.latest('created')
        return context
    
