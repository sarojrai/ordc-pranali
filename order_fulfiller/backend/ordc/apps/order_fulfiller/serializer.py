from rest_framework import serializers
from .models import Address, Customer, Order

class AddressSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Address
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):    

    # default_address = AddressSerializer(read_only=True)    
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):    

    customer = CustomerSerializer(read_only=True)
    billing_address = AddressSerializer(read_only=True)
    shipping_address = AddressSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

