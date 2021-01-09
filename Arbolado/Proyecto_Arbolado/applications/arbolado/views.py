# Django Modules 
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    View
)
# Django Models
from .models import Section
# Django Forms
from .forms import SectionForm, TreeForm

class SectionCreateView(CreateView):
    template_name = 'arbolado/register_section.html'
    model = Section
    form_class = SectionForm
    success_url = '.'
    
    def get_context_data(self, **kwargs):
        context = super(SectionCreateView, self).get_context_data(**kwargs)
        # Sending the TreeForm to the HTML template
        context["form_tree"] = TreeForm
        return context

    def form_valid(self, form):
        if self.request.is_ajax():
            data = dict()
            print( f'Solicitud Enviada: {self.request.POST}')
            print('---- AJAX REQUEST ----')
            section = form.save()
            data['id']     = section.id
            data['status'] = 'ok'
            return JsonResponse( data, status = 200 )
        else:
            return super(SectionCreateView, self).form_valid( form )
    
def TreeCreateView( request ):
    # Request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        data = {}
        # Get the form data, request.FILES for images, files and other kind of multimedia stuff
        form = TreeForm( request.POST, request.FILES )
        # Save the data and after fetch the object in an instance
        if form.is_valid():
            tree = form.save()
            data['id']          = tree.id
            data['name']        = tree.name
            data['species']     = tree.species.name
            data['description'] = tree.description
            data['status']      = tree.get_status_display()
            data['amount']      = tree.amount
            return JsonResponse(data, status = 200)
        else:
            # Some form errors occured
            return JsonResponse({ "error": form.errors}, status = 400)
    
    return JsonResponse({ "error": form.errors}, status = 400)
        

