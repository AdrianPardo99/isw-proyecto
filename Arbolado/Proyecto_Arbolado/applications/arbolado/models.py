# Django modules
from django.db import models
# Local Managers
from .managers import SectionManager
# Third Party Apps
from ckeditor_uploader.fields import RichTextUploadingField

# Módelo Alcaldía
class Town(models.Model):
    
    name = models.CharField(
        'Town name',
         max_length = 30
    )

    image = models.ImageField(
        'Image', 
        upload_to ='Towns', 
    )

    def __str__(self):
        return self.name 

# Modelo Especie
class Species(models.Model):
    
    name = models.CharField(
        'Species name',
         max_length = 50
    )

    class Meta:
        verbose_name = 'Species'
        verbose_name_plural = 'Species'

    def __str__(self):
        return self.name 

# Modelo Ubicación
class Location(models.Model):
    
    name = models.CharField(
        'Location name',
         max_length = 50
    )

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name 

# Modelo Árbol
class Tree(models.Model):

    STATUS_CHOICES = (
        ( '0', 'Muy Bueno' ),
        ( '1', 'Bueno' ),
        ( '2', 'Declinante Incipiente' ),
        ( '3', 'Declinante Severo' ),
        ( '4', 'Muerto' )
    )
    
    # Foreignkey from 'Species' model
    species = models.ForeignKey(
        Species, 
        on_delete = models.CASCADE
    )

    # django-ckeditor field 
    description = RichTextUploadingField()
    
    image = models.ImageField(
        'Image', 
        upload_to ='Trees', 
    )

    status = models.CharField(
        'Conservation Status', 
        max_length = 1, 
        choices = STATUS_CHOICES
    )

    amount = models.PositiveIntegerField('Amount') 
    
    class Meta:
        verbose_name = 'Tree'
        verbose_name_plural = 'Trees'

    def __str__(self):
        return str(self.id) + ': ' + self.species.name 

# Modelo Sección
class Section(models.Model):

    # Trees registered in the section  
    trees = models.ManyToManyField( Tree )

    # Location name
    location_name = models.CharField(
        'Location',
         max_length = 60
    )

    # Foreignkey from 'Location' model
    location_type = models.ForeignKey(
        Location, 
        on_delete = models.CASCADE
    )

    # Address provided by Google Maps
    address = models.TextField('Address')

    coords = models.CharField(
        'Coordinates',
         max_length = 200,
         blank = True
    )

    image = models.ImageField(
        'Image', 
        upload_to ='Sections', 
        null = True
    )

    # Foreignkey from 'Town' model
    town = models.ForeignKey(
        Town, 
        on_delete = models.CASCADE
    )

    # Linking the Manager with the model 
    objects = SectionManager()

    def __str__(self):
        return self.town.name + ': ' + self.location_name

