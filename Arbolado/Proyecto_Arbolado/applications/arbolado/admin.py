from django.contrib import admin
from .models import Town, Species, Tree, Section
# Register your models here.
admin.site.register( Town )
admin.site.register( Species )
admin.site.register( Tree )
admin.site.register( Section )