from django.db import models

class SectionManager(models.Manager):
    
    def search_section( self, location_name, location_type, town_name):
        """ Retrieving the sections with the given parameters """
        
        if len(location_name)>0 and len(location_type) == 0:
            print('LOCATION NAME')
            return self.filter(
                town__name = town_name,
                location_name__icontains = location_name
            )
        elif len(location_name) == 0 and len(location_type) > 0:
            print('LOCATION TYPE')
            return self.filter(
                town__name = town_name,
                location_type__name = location_type
            )
        else:
            print('ONLY TOWN NAME')
            return self.filter(
                town__name = town_name,
            )