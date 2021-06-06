# -*- coding: utf-8 -*-
__author__ = "Anil Kumar Gupta"
__copyright__ = "Copyright (©) 2018. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Django dependencies
from django.contrib import admin

# Project Related dependencies
from apps.client.models import Client, ClientAddress

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientAddress)
