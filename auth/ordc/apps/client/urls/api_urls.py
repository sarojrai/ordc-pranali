# -*- coding: utf-8 -*-
__author__ = "Anil Kumar Gupta"
__copyright__ = "Copyright (©) 2018. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Django related dependencies
from django.conf.urls import include, url

# Project related dependencies

from apps.client import views as api # ,customer_edit, customer_create, same_as_billing_add, customer_add_detail

clients_urls = [
                url(r'^$' ,api.ClientView.as_view({"get": "get_clients"}, name='clients')),
                url(r'^create$' ,api.ClientView.as_view({"post": "create_client"}, name='create_client')),
                #  url(r'^edit/(?P<pk>\w+)/$', customer_edit, name='customer_edit'),
                #  url(r'^customer_create/$', customer_create, name='customer_create'),
                #  url(r'^same_as_billing_add/$', same_as_billing_add, name='same_as_billing_add'),
                #  url(r'^customer_add_detail/$', customer_add_detail, name='customer_add_detail'),
                ]

urlpatterns = clients_urls
