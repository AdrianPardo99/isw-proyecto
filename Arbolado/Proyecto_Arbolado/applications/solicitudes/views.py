# Python Standard Modules
from datetime import date
# Django Utilities
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.generic import (
    CreateView,
    ListView,
)
# Django Local Models
from .models import SolicitudeRegister, Solicitude, SolicitudeReport
# Django Local Forms
from .forms import SolicitudeRegisterForm, SolicitudeReportForm
# External Application Forms
from applications.arbolado.forms import SectionForm, TreeForm
# Extra Funcions
from .utils import code_generator

class SolicitudeRegisterView( CreateView ):
    model = SolicitudeRegister
    # Reloading the Main Page
    success_url = '/'
    template_name = 'solicitudes/register_section.html'
    form_class    = SolicitudeRegisterForm

    def get_context_data(self, **kwargs):
        context = super(SolicitudeRegisterView, self).get_context_data(**kwargs)
        # Sending the TreeForm to the HTML template
        context["form_tree"] = TreeForm
        # Sending the SectionForm to the HTML template
        context["form_section"] = SectionForm
        return context

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        print( f'Formulario inválido: { form.cleaned_data } ')
        return self.render_to_response( context )

    def form_valid(self, form):
        if self.request.is_ajax():
            data = dict()
            print( f'Solicitud Enviada: {self.request.POST}')
            print('---- AJAX REQUEST ----')
            # Generating the solicitude code
            code = code_generator()
            # Getting the object instance without saving it in the Database 
            solicitud_register = form.save( commit = False )
            # Creating a Solicitude Instance
            solicitud = Solicitude(
                category        = '0',
                status          = '0',
                expedition_date = date.today()
            )
            # Saving the solicitud in the Database
            solicitud.save()
            # Adding the solicitude
            solicitud_register.solicitude = solicitud
            # Adding the solicitude code
            solicitud_register.solicitude_code = code
            # Saving the register request in the Database
            solicitud_register.save()
            # Setting up the JSON File Response
            data['id']     =  solicitud_register.id 
            data['status'] = 'ok'
            # Building up the email structure
            subject = 'Código de la Solicitud de Registro de una Sección de Arbolado'
            message = f"""
            Con el siguiente código puede darle seguimiento a su solicitud dentro del
            Sistema de Arbolado de la CDMX:
            
            Código: {code}"""
            email_sender   = 'kevingarciaescom@gmail.com'
            email_receiver = [ form.cleaned_data['email'], ]
            # Sending the email to the user
            send_mail(
                subject,
                message,
                email_sender,
                email_receiver
            )

            return JsonResponse( data, status = 200 )
        else:
            print("No ajax")
            return super(SolicitudeRegisterView, self).form_valid( form )


class SolicitudeReportView( CreateView ):
    template_name = 'solicitudes/register_report.html'
    model = SolicitudeReport
    success_url = '/'
    form_class = SolicitudeReportForm # 'form'

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        print( f'Formulario inválido: { form.cleaned_data } ')
        return self.render_to_response( context )

    def form_valid(self, form):
        if self.request.is_ajax():
            data = dict()
            print( f'Solicitud Enviada: {self.request.POST}')
            print('---- AJAX REQUEST ----')
            # Generating the solicitude code
            code = code_generator()
            # Getting the object instance without saving it in the Database
            solicitud_register = form.save( commit = False )
            # Creating a Solicitude Instance
            solicitud = Solicitude(
                category        = '1',
                status          = '0',
                expedition_date = date.today()
            )
            # Saving the solicitud in the Database
            solicitud.save()
            # Adding the solicitude
            solicitud_register.solicitude = solicitud
            # Adding the solicitude code
            solicitud_register.solicitude_code = code
            # Saving the register request in the Database
            solicitud_register.save()
            # Setting up the JSON File Response
            data['id']     =  solicitud_register.id
            data['status'] = 'ok'
            # Building up the email structure
            subject = 'Código de la Solicitud del Reporte de Incidencias'
            message = f"""
            Con el siguiente código puede darle seguimiento a su solicitud dentro del
            Sistema de Arbolado de la CDMX:

            Código: {code}"""
            email_sender   = 'kevingarciaescom@gmail.com'
            email_receiver = [ form.cleaned_data['email'], ]
            # Sending the email to the user
            send_mail(
                subject,
                message,
                email_sender,
                email_receiver
            )
            return JsonResponse( data, status = 200 )
        
        else:
            print("No ajax")
            return super(SolicitudeReportView, self).form_valid( form )

""" This view list all the request sended to register a new tree section """
class SolicitudesSeccionArboladoView(ListView):
    
    template_name = 'solicitudes/search_section.html'
    model = SolicitudeRegister
    context_object_name = 'solicitudes'
    paginate_by = 4

    def get_queryset(self):
        print(f'GET REQUEST: {self.request.GET}')
        # Retrieving the elements sended by GET Requests only 
        solicitude_code = self.request.GET.get('solicitud_id', '')
        # Searching the Sections with the given parameters
        query_result = SolicitudeRegister.objects.search_solicitud( solicitude_code )
        return query_result


class SolicitudesReportesView(ListView):

    template_name = 'solicitudes/search_report.html'
    model = SolicitudeReport
    context_object_name = 'solicitudes'
    paginate_by = 4

    def get_queryset(self):
        print(f'GET REQUEST: {self.request.GET}')
        # Retrieving the elements sended by GET Requests only 
        solicitude_code = self.request.GET.get('solicitud_id', '')
        # Searching the Sections with the given parameters
        query_result = SolicitudeReport.objects.search_solicitud( solicitude_code )
        return query_result
    
 
    
 

    

