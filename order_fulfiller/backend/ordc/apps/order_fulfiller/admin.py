from django.contrib import admin
from apps.order_fulfiller.models import Order, Customer, Address

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Address)