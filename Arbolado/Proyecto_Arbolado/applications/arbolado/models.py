# Django modules
from django.db import models
# Third Party Apps
from ckeditor_uploader.fields import RichTextUploadingField

# Módelo Alcaldía
class Town(models.Model):
    
    name = models.CharField(
        'Town name',
         max_length = 30
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

# Modelo Árbol
class Tree(models.Model):

    STATUS_CHOICES = (
        ( '0', 'Muy Bueno' ),
        ( '1', 'Bueno' ),
        ( '2', 'Declinante Incipiente' ),
        ( '3', 'Declinante Severo' ),
        ( '4', 'Muerto' )
    )
    
    name = models.CharField(
        'Tree name',
         max_length = 50
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
        upload_to='Trees', 
    )

    status = models.CharField(
        'Conservation Status', 
        max_length = 1, 
        choices = STATUS_CHOICES
    )

    amount = models.PositiveIntegerField(
        'Amount',
        default = 0
    ) 

    class Meta:
        verbose_name = 'Tree'
        verbose_name_plural = 'Trees'

    def __str__(self):
        return self.name + ': ' + str(self.amount)

# Modelo Sección
class Section(models.Model):
     
    trees = models.ManyToManyField( Tree )

    location = models.CharField(
        'Location',
         max_length = 60
    )

    address = models.CharField(
        'Address',
         max_length = 120
    )

    coords = models.CharField(
        'Coordinates',
         max_length = 120,
         blank = True
    )

    # Foreignkey from 'Town' model
    town = models.ForeignKey(
        Town, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.location + ': ' + self.town.name
