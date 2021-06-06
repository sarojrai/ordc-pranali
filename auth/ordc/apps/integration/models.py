from django.db import models
from apps.client.models import Client
# Create your models here.


class ScmServiceType(models.Model):
    """
    Brand Websites: [Shopify, Magento] Market Places: [Amazon,Flipkart]
    """
    
    code	 		           = models.CharField(max_length=50, unique=True, db_index=True)
    description 		       = models.CharField(max_length=150, blank=True, null=True)
    added_on 			       = models.DateTimeField(auto_now_add=True, db_index=True) 
    updated_on 			       = models.DateTimeField(auto_now_add=True, db_index=True) 
    status 			           = models.FloatField(default=0,db_index=True)

    def __str__(self):
        return self.code

class ScmService(models.Model):
    """
    Integration_Identifier_key1, Integration_Identifier_value2
    """
    scm_type                         = models.ForeignKey(ScmServiceType, null=True, blank=True, on_delete=models.SET_NULL)
    client                           = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    integration_Identifier_key1	     = models.CharField(max_length=50, blank=True, null=True)
    integration_Identifier_value1 	 = models.CharField(max_length=50, blank=True, null=True)
    integration_Identifier_key2      = models.CharField(max_length=50, blank=True, null=True)
    integration_Identifier_value2    = models.CharField(max_length=50, blank=True, null=True)
    credential_key1	                 = models.CharField(max_length=50, blank=True, null=True)
    credential_vaue1	             = models.CharField(max_length=50, blank=True, null=True)
    credential_key2                  = models.CharField(max_length=50, blank=True, null=True)
    credential_vaue2	             = models.CharField(max_length=50, blank=True, null=True)
    added_on 			             = models.DateTimeField(auto_now_add=True, db_index=True) 
    updated_on 			             = models.DateTimeField(auto_now_add=True, db_index=True) 
    status 			                 = models.FloatField(default=0,db_index=True)

    

