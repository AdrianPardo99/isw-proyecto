from django.urls import path

from . import views

app_name = "solicitudes_app"

urlpatterns = [
    path(
        'solicitudes/register/section/report', 
        views.SolicitudeRegisterView.as_view(),
        name='solicitudes_registro',
    ), 
    
]