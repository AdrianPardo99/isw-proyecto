from django.urls import path

from . import views

app_name = "solicitudes_app"

urlpatterns = [
    
    path(
        'solicitudes/section/register', 
        views.SolicitudeRegisterView.as_view(),
        name='section_register',
    ), 

    path(
        'solicitudes/trees/report', 
        views.SolicitudeReportView.as_view(),
        name='trees_report',
    ),
    
    # Consultas
    path(
        'solicitudes/search/section/report', 
        views.SolicitudesSeccionArboladoView.as_view(),
        name='search_section_report',
    ),

    path(
        'solicitudes/search/issues/report', 
        views.SolicitudesReportesView.as_view(),
        name='search_issues_report',
    ),

]