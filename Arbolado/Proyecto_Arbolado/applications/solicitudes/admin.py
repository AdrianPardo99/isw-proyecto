from django.contrib import admin
from .models import Solicitude, SolicitudeRegister, SolicitudeReport
# Register your models here.
admin.site.register( Solicitude )
admin.site.register( SolicitudeRegister )
admin.site.register( SolicitudeReport )
