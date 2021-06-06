# -*- coding: utf-8 -*-
__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Django related dependencies
from django.conf.urls import url

# Project Related dependencies
from  apps.integration.views import api_views as api


service_urls = [
    url(r'^type/', api.IntegrationView.as_view({"get": "get_service_type"}, name="service_type")),
    url(r'^$', api.IntegrationView.as_view({"get": "get_service"}, name="service")),
    url(r'^create$', api.IntegrationView.as_view({"post": "create_service"}, name="create_service")),
   
]

other_urls = []

# Main URL
urlpatterns = service_urls+other_urls
