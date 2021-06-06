# -*- coding: utf-8 -*-
__author__ = "Saroj Kumar Rai"
__copyright__ = "Copyright (©) 2021. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Django related dependencies
from django.conf.urls import url

# Project Related dependencies
from apps.ecommerce.views import api_views as views
web_urls = [ 
    url(r'^product-category/$', views.product_category, name="product_category"),
    url(r'^product-source/$' , views.product_source,name="product-source"),
]
## Main URL
# urlpatterns = web_urls + app_urls
urlpatterns = web_urls
