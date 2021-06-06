# -*- coding: utf-8 -*-
__author__="Anil Kumar Gupta"
__copyright__="Copyright (©) 2017. ORDC. All rights reserved."
__credits__=["ORDC"]

# Django related dependencies
from django.db import models

class CommunicationMode(models.Model):
    """
    WHATSAPP, SMS, IVR
    """
    code	 		           = models.CharField(max_length=50, unique=True, db_index=True)
    description 		       = models.CharField(max_length=150, blank=True, null=True)
    priority                   = models.IntegerField(default=1,db_index=True) ## 1 is highest
    sequence                   = models.IntegerField(default=1,db_index=True) ## 1 is first
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True) 
    status 			           = models.FloatField(default=0,db_index=True)

    def __str__(self):
        return self.code

class CommunicationEvent(models.Model):
    """
    Payment Type: COD, PPD, ALL
    """
    code	 		           = models.CharField(max_length=50, unique=True, db_index=True)
    description 		       = models.CharField(max_length=150, blank=True, null=True)
    notification_template 	   = models.CharField(max_length=150, blank=True, null=True)
    sequence                   = models.IntegerField(default=1,db_index=True) ## 1 is first
    is_attachement             = models.BooleanField(default=False)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True)
    status 			           = models.FloatField(default=0,db_index=True)
    def __str__(self):
        return self.code

class CommunicationChannel(models.Model):
    """
    gupshup, whatsapp, heptic
    """
    mode                       = models.ForeignKey(CommunicationMode, on_delete=models.SET_NULL, blank=True, null=True)
    code	 		           = models.CharField(max_length=50, unique=True, db_index=True)
    description 		       = models.CharField(max_length=150, blank=True, null=True)
    url 		               = models.CharField(max_length=150, blank=True, null=True)
    credentials 		       = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True) 
    status 			           = models.FloatField(default=0,db_index=True)

    def __str__(self):
        return self.code +"-"+ self.mode.code

class ClientCommunication(models.Model):
    """
    Client and Communication config
    """
    channel                    = models.ForeignKey(CommunicationChannel, on_delete=models.SET_NULL, blank=True, null=True)
    client                     = models.CharField(max_length=50, db_index=True)
    event                      = models.ForeignKey(CommunicationEvent, on_delete=models.SET_NULL, blank=True, null=True)
    notification_template 	   = models.CharField(max_length=150, blank=True, null=True)
    sequence                   = models.IntegerField(default=1,db_index=True) ## 1 is first
    priority                   = models.IntegerField(default=1,db_index=True) ## 1 is highest
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True) 
    status 			           = models.FloatField(default=0,db_index=True)


