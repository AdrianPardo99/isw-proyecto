from django.db import models
# External model application
from applications.arbolado.models import Section

class Person(models.Model):
    
    full_name = models.CharField(
        'Name', 
        max_length = 60
    )

    email = models.EmailField(
        'Email', 
        unique = True 
    )

    age = models.PositiveIntegerField(
        'Age',
        default = 0
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
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return str( self.expedition_date )


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

    class Meta:
        verbose_name = 'Register Request'
        verbose_name_plural = 'Register Requests'

    def __str__(self):
        return str( self.solicitude.expedition_date )


