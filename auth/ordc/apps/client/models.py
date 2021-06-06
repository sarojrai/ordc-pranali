# -*- coding: utf-8 -*-
__author__ = "Anil Kumar Gupta"
__copyright__ = "Copyright (©) 2018. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# python dependencies

# Django related dependencies
from django.db import models
from django.contrib.auth.models import User

# Project related dependencies
from apps.authentication.models import EmployeeMaster


BILLING_CHOICES = (('Weekly', 'Weekly'), 
                   ('Fortnight', 'Fortnight'), #make anothe table
                   ('Monthly', 'Monthly')
                   )
SHIPPER_TYPE = ((0, 'Normal'), 
                (1, 'To Pay')
               )

class NamedUser(EmployeeMaster):
    class Meta:
        proxy=True

    def __unicode__(self):
        return self.get_name_with_employee_code()

CUST_TYPE  = (  ("CUST","Customer"),
                ("MFR","Manufacturer"),
                ("SPLR","Supplier"),
                ("WMS","WMS"),
                ("LSTC","Logistic Partner"),
                ("BRND","Brand Website"),
                ("MRKT","Market Place"),
            )

class Client(models.Model):
    ## General Info
    name                            = models.CharField(max_length=100)
    code                            = models.CharField(max_length=30 , unique = True)
    website                         = models.CharField(max_length=200, blank=True, null=True)
    email                           = models.CharField(max_length=200, blank=True, null=True)
    referred_by                     = models.CharField(max_length=30, blank=True, null=True)
    client_type                   = models.CharField(max_length=10, default='CUST', choices=CUST_TYPE) 
    mobile                          = models.CharField(max_length =15, blank=True, null=True)
    ##contact person details
    contact_person                  = models.CharField(max_length=50, blank=True, null=True)
    contact_phone                   = models.CharField(max_length=15, blank=True, null=True)
    contact_email                   = models.CharField(max_length=150, blank=True, null=True)
    
    contract_from                   = models.DateField()
    contract_to                     = models.DateField()
    created_by                      = models.ForeignKey(User, related_name='created_by', blank=True, null=True, on_delete=models.SET_NULL)
    updated_by                      = models.ForeignKey(User, related_name='updated_by', blank=True, null=True, on_delete=models.SET_NULL)
    added_on                        = models.DateTimeField(auto_now_add=True, db_index = True)
    updated_on                      = models.DateTimeField(auto_now=True, db_index = True)
    status                          = models.FloatField(default = 0, db_index = True)
    ## Activation Info
    activation_status               = models.BooleanField(default = True)
    activation_date                 = models.DateField(blank=True, null=True)
    activated_by                    = models.ForeignKey(User, related_name='activation_by', blank=True, null=True, on_delete=models.SET_NULL)
    deactivation_date               = models.DateField()
    ## Billing Info
    billing_schedule                = models.IntegerField(default=7)
    day_of_billing                  = models.SmallIntegerField(default=7)
    remittance_cycle                = models.SmallIntegerField(default=7)
    credit_limit                    = models.IntegerField(default = 10000)
    credit_period                   = models.IntegerField(default = 10)
    bill_delivery_email             = models.BooleanField(default=True)
    bill_delivery_hand              = models.BooleanField(default=True)
    latest_invoice_date             = models.DateField(blank=True, null=True)
    next_bill_date                  = models.DateField(blank=True, null=True)
    ## Imp Info 
    approved                        = models.ForeignKey(NamedUser, related_name='approver', blank=True, null=True, on_delete=models.SET_NULL)
    authorized                      = models.ForeignKey(NamedUser, related_name='authorizer', blank=True, null=True, on_delete=models.SET_NULL)
    ## Domain
    industry                        = models.CharField(max_length=100, blank=True, null=True)
    product_category                = models.CharField(max_length=150, blank=True, null=True)
    product_sales                   = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name + " - " + self.code

    def get_status(self):
        s = {1.0:'Active', 0.0:'Inactive'}
        return s[self.status]

    def shipping_address(self):
        ship = self.clientaddress_set.filter(address_type_id=4).values('address1','address2','address3', \
                                   'city__name', 'contact_person', 'email', 'landmark', 'mobile', 'pincode',\
                                   'state__code', 'status','telephone', 'gst__gst_number','id', 'state__country__code')
        return ship

    def billing_address(self):
        bill = self.clientaddress_set.filter(address_type_id=3).values('address1','address2','address3', \
                                   'city__name', 'contact_person', 'email', 'landmark', 'mobile', 'pincode',\
                                   'state__code', 'status','telephone', 'gst__gst_number', 'id','state__country__code')
        return bill

    def get_supplier_detail(self):
        supplier_detail = {}
        supplier_detail['supplier_id'] = self.id
        supplier_detail['supplier_name'] = self.name
        supplier_detail['supplier_code'] = self.code
        try:
            d = self.billing_address()[-1]
            supplier_detail['supplier_add'] = d['address1']+d['address1']+d['address1']
            supplier_detail['supplier_pincode'] = d['pincode']
            supplier_detail['supplier_city'] = d['city__name']
            supplier_detail['supplier_state'] = d['state__code']
        except:
            supplier_detail['supplier_add'] = "not found"
            supplier_detail['supplier_pincode'] = "not found"
            supplier_detail['supplier_city'] = "not found"
            supplier_detail['supplier_state'] = "not found"

        supplier_detail['supplier_gst_number'] = "aaa"
        supplier_detail['supplier_email'] = self.email
        supplier_detail['supplier_website'] = self.website
        return supplier_detail


"""
class Vendor(models.Model):
   class Meta:
      	abstract = True

class Cutomer(Vendor):
   pass

class Supplier(Vendor):
   pass
      
##Need to replace supllier cutomer and vendor or same kind of models by using meta inheritance
"""
class AddressType(models.Model):
      #("HQ", 'HEAD-'),
      #("REGISTERED", 'REGISTERED'),
      #("DEFAULT-BILLING", 'DEFAULT-BILLING'),
      #("DEFAULT-SHIPPING", 'DEFAULT-SHIPPING')
    code 			                = models.CharField(max_length =15, unique=True)
    name			                = models.CharField(max_length =50, blank=True, null=True)

class ClientAddress(models.Model):
    client                          = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    address_type          	        = models.ForeignKey(AddressType, null=True, blank=True, on_delete=models.SET_NULL)
    address1                        = models.CharField(max_length =250, blank=True, null=True)
    address2                        = models.CharField(max_length =250, blank=True, null=True)
    address3                        = models.CharField(max_length =250, blank=True, null=True)
    pincode                         = models.IntegerField()
    city                            = models.ForeignKey('authentication.City', null=True, blank=True, on_delete=models.SET_NULL)
    state                           = models.ForeignKey('authentication.State', null=True, blank=True, on_delete=models.SET_NULL)
    contact_person                  = models.CharField(max_length =250, blank=True, null=True)
    mobile                          = models.CharField(max_length =15, blank=True, null=True)
    telephone                       = models.CharField(max_length =15, blank=True, null=True)
    email                           = models.CharField(max_length =50, blank=True, null=True)
    landmark                        = models.CharField(max_length =50, blank=True, null=True)
    added_on                        = models.DateTimeField(auto_now_add=True, db_index = True)
    updated_on                      = models.DateTimeField(auto_now=True, db_index = True)
    status                          = models.FloatField(default = 0, db_index = True)
    ## Bank details
    bank_name                       = models.CharField(max_length =150, blank=True, null=True)
    ifsc_code                       = models.CharField(max_length =20, blank=True, null=True)
    account_no                      = models.CharField(max_length =30, blank=True, null=True)


class GSTServiceType(models.Model):
    service_type                    = models.CharField(max_length=100, null=True, blank=True)
    service_code                    = models.CharField(max_length=100, unique = True)
    sac_code                        = models.CharField(max_length=100, unique = True)
    hsn_code                        = models.CharField(max_length=100, unique = True)
    tax_rate                        = models.FloatField()
    status                          = models.FloatField(default =0, null=True, blank=True,db_index = True)
    added_on                        = models.DateTimeField(auto_now_add = True, db_index = True)
    updated_on                      = models.DateTimeField(auto_now=True, null=True, blank=True, db_index = True)
    def __str__(self):
        return self.service_type

class GSTStateRate(models.Model):
    state                           = models.ForeignKey('authentication.State', null=True, blank=True, on_delete=models.SET_NULL, related_name = "gst_state")
    service_type                    = models.ForeignKey('GSTServiceType', null=True, blank=True, on_delete=models.SET_NULL)
    cgstn                           = models.FloatField(null=True, blank=True)
    sgstn                           = models.FloatField(null=True, blank=True)
    igstn                           = models.FloatField(null=True, blank=True)
    status                          = models.IntegerField(default=0, null=True, blank=True, db_index = True)
    added_on                        = models.DateTimeField(auto_now_add = True, db_index = True)
    updated_on                      = models.DateTimeField(auto_now=True, null=True, blank=True, db_index = True)
    def __str__(self):
        return self.state.name


class GST(models.Model):
    ## GST Info
    client_address		        = models.ForeignKey(ClientAddress, null=True, blank=True, on_delete=models.SET_NULL)
    pan_number                      = models.CharField(max_length=20, blank=True, null=True)
    gst_number                      = models.CharField(max_length=30, blank=True, null=True)
    state_gst_code                  = models.CharField(max_length=10, blank=True, null=True)
    regtration_type                 = models.SmallIntegerField(default=0,db_index=True) #0=Individual, 1 = ISD
    default_reg                     = models.CharField(max_length=1, null=True, blank=True)
    service_type                    = models.ForeignKey(GSTServiceType, null = True, blank =True, on_delete=models.SET_NULL) #11: Other *******
    USE_FOR_CHOICES                 = ((1,"All"),(2,"Vendor"))
    use_for                         = models.SmallIntegerField(default=1,choices = USE_FOR_CHOICES, db_index=True)
    invoice_type                    = models.SmallIntegerField(default=1,db_index=True) #1 = Invoice , 2 - Debit Note,3 - Credit Note