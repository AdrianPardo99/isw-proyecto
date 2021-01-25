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

    path(
        'arbolado/delete/tree',
        views.TreeDeleteView,
        name = 'delete_tree',
    ),

    path(
        'arbolado/alcaldias/',
        views.TownListView.as_view(),
        name = 'arbolado_alcaldias',
    ),

    path(
        'arbolado/alcaldias/sections/<name>',
        views.ListSectionsByTown.as_view(),
        name = 'arbolado_sections'
    ),

    path(
        'arbolado/alcaldias/section/detail/<int:pk>',
        views.SectionDetailView.as_view(),
        name = 'arbolado_section_detail'
    ),
]

