# -*- coding: utf-8 -*-
__author__="Anil Kumar Gupta"
__copyright__="Copyright (©) 2017. ORDC. All rights reserved."
__credits__=["ORDC"]

# Django related dependencies
import jsonfield
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Project Related dependencies

class ProductCategory(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code

class SourceType(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code

class BrandWebsite(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code

class MarketPlace(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code

class CourierPartner(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code

class WarehouseManagement(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code

class CommunicationMode(models.Model):
    code 	                   = models.CharField(max_length=50, unique=True, db_index=True)
    description                = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    
    def __str__(self):
        return self.code


class ClientOnboarding(models.Model):
    client_name 	        = models.CharField(max_length=150, unique=True, db_index=True,null=False)
    source                  = models.CharField(max_length=150, blank=True, null=True)
    address1                = models.CharField(max_length=150, blank=True, null=True)
    address2                = models.CharField(max_length=150, blank=True, null=True)
    address3                = models.CharField(max_length=150, blank=True, null=True)
    state                   = models.CharField(max_length=150, blank=True, null=True)
    city                    = models.CharField(max_length=150, blank=True, null=True)
    pincode                 = models.CharField(max_length=150, blank=True, null=True)
    product_category        = models.CharField(max_length=150, blank=True, null=True)
    salesValue              = models.CharField(max_length=150, blank=True, null=True)
    bank_details            = jsonfield.JSONField()
    contact_details         = jsonfield.JSONField()
    brand_website           = models.CharField(max_length=150, blank=True, null=True)
    warehouse_mgmt          = models.CharField(max_length=150, blank=True, null=True)
    courier_partner         = models.CharField(max_length=150, blank=True, null=True)
    mktplace_websites       = jsonfield.JSONField()
    
    mode_of_notification    = jsonfield.JSONField()
    order_types             = jsonfield.JSONField()
    notification_method     = models.CharField(max_length=150, blank=True, null=True)
    first_mode_of_notification    = models.CharField(max_length=150, blank=True, null=True)
    add_calaculation_feature      = models.BooleanField(default=False)
    no_of_reminders                 = jsonfield.JSONField()
    notification_mode_priority      = jsonfield.JSONField()
    sequence_ndr_shipment_orders    = jsonfield.JSONField()
    status 			                = models.FloatField(default=0,db_index=True)
    added_on 			    = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on 			    = models.DateTimeField(auto_now=True, db_index=True)
    
    def __str__(self):
        return self.name


