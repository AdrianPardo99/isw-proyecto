from django.db import models
# External model application
from applications.arbolado.models import Section, Town
# Third Party Apps
from ckeditor_uploader.fields import RichTextUploadingField
# Local Maganagers
from .managers import SolicitudeManager



class Person(models.Model):
    
    full_name = models.CharField(
        'Name', 
        max_length = 60
    )

    email = models.EmailField(
        'Email', 
        unique = False 
    )

    age = models.PositiveIntegerField(
        'Age',
        default = 0,
    )

    class Meta:
        # This model will not be created in the Data Base
        abstract = True

    def __str__(self):
        return str(self.id) + '. ' + self.full_name


class Solicitude( models.Model ):

    STATUS_CHOICES = (
        ('0', 'Pendiente'),
        ('1', 'Atendida'),
    )

    CATEGORY_CHOICES = (
        ('0', 'Registro'),
        ('1', 'Reporte'),
    )

    category = models.CharField(
        max_length = 1, 
        choices = CATEGORY_CHOICES, 
        blank = True
    )

    status = models.CharField(
        max_length = 1, 
        choices = STATUS_CHOICES, 
        blank = True
    )

    expedition_date = models.DateField(
        'Expedition Date', 
        auto_now = False, 
        auto_now_add = False
    )

    class Meta:
        verbose_name = 'Request Information'
        verbose_name_plural = 'Requests Information'
    
    # Access to the real value of choices type field: .get_ChoicesAttributeName_display()
    def __str__(self):
        return str( self.expedition_date ) + ': ' + self.get_category_display() + ' Arbolado'


class SolicitudeRegister( Person ):

    section = models.ForeignKey(
        Section, 
        on_delete = models.CASCADE
    )

    solicitude = models.ForeignKey(
        Solicitude, 
        on_delete = models.CASCADE
    )

    solicitude_code = models.CharField(
        'Solicitud Code', 
        max_length = 8,
        default = '000000'
    )

    # Linking the Manager with the model 
    objects = SolicitudeManager()

    class Meta:
        verbose_name = 'Register Request'
        verbose_name_plural = 'Register Requests'

    def __str__(self):
        return str( self.solicitude_code) + ': Expedida el ' + str( self.solicitude.expedition_date )

class SolicitudeReport(Person):

    STATUS_CHOICES = (
        ('0', 'Alto'),
        ('1', 'Medio'),
        ('2', 'Bajo')
    )

    image = models.ImageField(
        'Image', 
        upload_to ='Reports', 
    )

    description = models.TextField('Description')

    address  = models.TextField('Dirección')

    # Foreignkey from 'Town' model
    town = models.ForeignKey(
        Town, 
        on_delete = models.CASCADE
    )

    # Foreignkey from 'Solicitude' model
    solicitude = models.ForeignKey(
        Solicitude, 
        on_delete = models.CASCADE
    )

    status = models.CharField(
        'Nivel de Urgencia', 
        max_length = 1,
        choices = STATUS_CHOICES, 
        blank = True
    )

    solicitude_code = models.CharField(
        'Solicitud Code', 
        max_length = 8,
        default = '000000'
    )

    # Linking the Manager with the model 
    objects = SolicitudeManager()

    class Meta:
        verbose_name = 'Register Report'
        verbose_name_plural = 'Register Reports'

    def __str__(self):
        return str( self.solicitude_code) + ': Expedida el ' + str( self.solicitude.expedition_date )





