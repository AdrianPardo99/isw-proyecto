from django.db import models

class SolicitudeManager(models.Manager):
    def search_solicitud(self, solicitude_code):
        if len(solicitude_code)>0:
            print('Searching by code...')
            return self.filter(
                solicitude_code = solicitude_code
            )
        else:
            print('Returning all the avaliable codes')
            return self.all()
