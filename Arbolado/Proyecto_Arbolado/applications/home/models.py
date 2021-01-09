from django.db import models

# Third Part Applications
from model_utils.models import TimeStampedModel 

# Modelo: Home
class Home(TimeStampedModel):
    
    """ Main Page Model """
    
    title = models.CharField(
        'Title name',
         max_length=60
    )

    about_text = models.CharField(
        'About title', 
        max_length=50
    )

    image = models.ImageField(
        'Background Image', 
        upload_to='Home' 
    )
    
    # Datos Footer 
    contact_email = models.EmailField(
        'Contact Email', 
        blank = True,
        null  = True
    )

    contact_phone = models.CharField(
        'Contact Phone', 
        max_length=20
    )

    contact_message = models.CharField(
        'Contact Message', 
        max_length=30
    )

    class Meta:
        verbose_name        = 'Main Page'
        verbose_name_plural = 'Main Page'

    def __str__(self):
        return self.title   

