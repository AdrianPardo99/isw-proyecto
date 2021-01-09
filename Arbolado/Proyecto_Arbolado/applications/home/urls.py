from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        # Al dejarlo en blanco indicamos que sea la página principal
        '', 
        views.HomePageView.as_view(),
        name = 'index',
    ), 
    
]