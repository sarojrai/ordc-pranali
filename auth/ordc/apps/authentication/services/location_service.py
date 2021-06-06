
## Project Related
from apps.authentication.models import ServiceCentre, Organisation, City
from django.db.models import Q, F

import logging
logger = logging.getLogger(__name__)

class LocationManager:
    def __init__(self):
        self.test = None

    def get_service_centre(self):
        """
        DOCString
        """
        try:
            sc = ServiceCentre.objects.all().values("id","code", "name")
            sc = list(sc)
            return True, sc
        except Exception as e:
            return False, []
    
    def get_organisation(self, requested_data, **kwargs):
        """
        DOCString
        """
        message = "Failed"
        try:
            org = Organisation.objects.all().filter(**kwargs).values()
            org = list(org)
            message = "Organisations Details Fetched Successfully !"
            return True, message, org
        except Exception as e:
            return False, message, []

    def get_cities(self):
        """
        Returns city list
        """
        try:
            cities = City.objects.all().values("name", "code", state_name=F("state__name"), state_code=F("state__code"))
            cities = list(cities)
            return True, cities
        except Exception as e:
            return False, []
