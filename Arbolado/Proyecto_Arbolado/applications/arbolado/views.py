# Django Modules 
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    ListView,
)
# Django Models
from .models import Section, Tree, Town, Location
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
            data['species']     = tree.species.name
            data['description'] = tree.description
            data['status']      = tree.get_status_display()
            data['amount']      = tree.amount
            return JsonResponse(data, status = 200)
        else:
            # Some form errors occured
            return JsonResponse({ "error": form.errors}, status = 400)
    
    return JsonResponse({ "error": form.errors}, status = 400)


def TreeDeleteView( request ):
    # Request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        data = {}
        print(f'SOLICITUD ENVIADA PARA ELIMINAR EL ÁRBOL {request.POST}')
        # Getting the id form the POST Request
        id_tree = request.POST['id_tree']
        # Deleting the tree from the Database
        Tree.objects.filter( id = id_tree ).delete()
        # Sending the JSON Response to the Front-End
        data['status'] = 'Árbol Eliminado'
        return JsonResponse(data, status = 200)
    else:
        # Some form errors occured
        return JsonResponse({ "error": 'No Response'}, status = 400)
    
    return JsonResponse({ "error": 'No Response'}, status = 400)


class TownListView(ListView):
    template_name = 'arbolado/alcaldias.html'
    model = Town
    context_object_name = 'towns'
    ordering = 'name'
    

class ListSectionsByTown(ListView):
    template_name = 'arbolado/alcaldia_secciones.html'
    model = Section
    ordering = 'location_name'
    
    context_object_name = 'sections'
    def get_queryset(self):
        print(f'GET REQUEST: {self.request.GET}')
        # Retrieving the elements sended by GET Requests only 
        location_name = self.request.GET.get('kword', '')
        location_type = self.request.GET.get('location', '')
        print(f'KWARGS DICTIONARY: {self.kwargs}')
        # Retrieving the element from the URL taged with 'name' this is specified in the urls.py file
        # arbolado/alcaldias/sections/<name> -> <name> element that was sended in the URL
        town_name = self.kwargs['name']
        # Searching the Sections with the given parameters
        query_result = Section.objects.search_section( location_name, location_type, town_name)
        return query_result
    
    def get_context_data(self, **kwargs):
        context = super(ListSectionsByTown, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context
    


    
    

