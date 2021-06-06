import uuid
import datetime
from django.utils import timezone
from django.db import models

class Customer(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    orders_count = models.IntegerField(default=0)
    state = models.CharField(max_length=255, null=True, blank=True)
    total_spent = models.CharField(max_length=255, null=True, blank=True)
    last_order_id = models.CharField(max_length=255, null=True, blank=True)
    verified_email = models.BooleanField(default=False)
    tax_exempt = models.BooleanField(default=False)
    phone = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_blacklisted = models.BooleanField(default=False)

class Address(models.Model):
    address_type =  models.CharField(max_length=255, null=True, blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='address_customer')
    first_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    province_code = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    country_name = models.CharField(max_length=255, null=True, blank=True)
    default = models.BooleanField(default=False)    
    company = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class Order(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    order_number = models.CharField(max_length=255, null=True, blank=True) # by market place
    app_id = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='order_customer')
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    is_blacklisted = models.BooleanField(default=False)
    status = models.CharField(max_length=255, null=True, blank=True)# in our system - float numbers - current status of order
    gross_amount = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    discount = models.CharField(max_length=255, null=True, blank=True)
    tax = models.CharField(max_length=255, null=True, blank=True)
    payload_data = models.JSONField() # payload data
    source_type = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    source_website = models.CharField(max_length=1024, null=True, blank=True)
    client_id = models.CharField(max_length=255, null=True, blank=True)# emami
    source_status = models.CharField(max_length=255, null=True, blank=True)# on shopify
    billing_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='billing_address') 
    shipping_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='shipping_address') 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255, default='SYSTEM')
    updated_by = models.CharField(max_length=255, default='SYSTEM')
