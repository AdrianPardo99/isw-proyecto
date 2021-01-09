# Aquí declararemos las variables globales que queramos que se vean reflejadas en todo el proyecto 
from applications.home.models import Home 
# Procesor para recuperar el teléfono y correo del registro home 
# Toda función que ejecutará un context_processors debe llevar el 
# parámetro 'request'
def home_contact(request):
    # Recuperamos el último registro hecho en el modelo Home
    home = Home.objects.latest('created')
    # Todos los context_processors retornaran un diccionario
    return {
        'contact_phone'   : home.contact_phone,
        'contact_email'   : home.contact_email,
        'contact_message' : home.contact_message,
    }
