from django.urls import path
from . import views

app_name = "arbolado_app"

urlpatterns = [
    
    path(
        'arbolado/register/section', 
        views.SectionCreateView.as_view(),
        name = 'arbolado_section',
    ), 

    path(
        'arbolado/register/tree', 
        views.TreeCreateView,
        name = 'register_tree',
    ), 
    
]