# -*- coding: utf-8 -*-
__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Django related dependencies
from django.conf.urls import url

# Project Related dependencies
from  apps.notification.views import api_views as api


communication_urls = [
    url(r'^modes/', api.NotificationView.as_view({"get": "get_communication_modes"}, name="modes")),
    url(r'^channels/', api.NotificationView.as_view({"get": "get_communication_channels"}, name="channels")),
    url(r'^events/', api.NotificationView.as_view({"get": "get_communication_events"}, name="events")),
    url(r'^clients/', api.NotificationView.as_view({"get": "get_client_communication"}, name="client_communication")),
    url(r'^config/', api.NotificationView.as_view({"post": "create_client_communication"}, name="client_communication")),
    url(r'^notify/', api.NotificationView.as_view({"post": "notify"}, name="notify")),
]

other_urls = []

# Main URL
urlpatterns = communication_urls+other_urls
