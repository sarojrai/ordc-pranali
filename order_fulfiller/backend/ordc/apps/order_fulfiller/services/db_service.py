import traceback
from django.db import transaction, IntegrityError

from apps.order_fulfiller.models import Order, Customer, Address
from apps.order_fulfiller.serializer import OrderSerializer
from apps.order_fulfiller.constants import Constant as C

@transaction.atomic
def create_order(filtered_data):
    tra = transaction.savepoint()
    try:
        order_details = filtered_data['order_details']
        customer = filtered_data['customer_details']
        default_address = filtered_data['default_address_details']
        billing_address = order_details['billing_address']
        shipping_address = order_details['shipping_address']

        customer_obj = Customer(**customer)
        customer_obj.save()

        billing_address['customer_id'] = customer_obj.id
        shipping_address['customer_id'] = customer_obj.id
        default_address['customer_id'] = customer_obj.id
        default_address['default'] = True
        billing_address['address_type'] = 'BILLING'
        shipping_address['address_type'] = 'SHIPPING'
        
        default_address_obj = Address(**default_address)
        default_address_obj.save()
        billing_address_obj = Address(**billing_address)
        billing_address_obj.save()
        shipping_address_obj = Address(**shipping_address)
        shipping_address_obj.save()

        order_details['customer_id'] = customer_obj.id
        order_details['billing_address'] = billing_address_obj
        order_details['shipping_address'] = shipping_address_obj
        order_details[C.PAYLOAD_DATA] = filtered_data[C.PAYLOAD_DATA]

        order_obj = Order(**order_details)
        order_obj.save()

        transaction.savepoint_commit(tra)
        return {"order_id": order_obj.id}
    except IntegrityError:
        traceback.print_exc()
        transaction.savepoint_rollback(tra)
        return False
    

def get_all_orders():
    try:
        order_list = []
        orders = Order.objects.order_by('-updated_at')
        serializer = OrderSerializer(orders, many=True)
        order_data = serializer.data
        for order in order_data:
            metadata = {}    
            metadata[C.ORDER_NO[0]] = order[C.ORDER_NO[0]]
            metadata[C.SOURCE[0]] = '{} - {}'.format(order[C.SOURCE_TYPE[0]].title(), order[C.SOURCE[0]].title())
            metadata[C.PAYMENT_TYPE[0]] = order[C.PAYMENT_TYPE[0]]
            metadata[C.GROSS_AMOUNT[0]] = '{} {}'.format(order[C.CURRENCY[0]], order[C.GROSS_AMOUNT[0]])
            metadata[C.STATUS[0]] = order[C.STATUS[0]].replace('_', ' ').title()
            metadata[C.IS_BLACKLISTED[0]] = 'YES' if order[C.IS_BLACKLISTED[0]] else 'NO'
            metadata[C.CREATED_AT[0]] = order[C.CREATED_AT[0]].split('T')[0]
            metadata[C.UPDATED_AT[0]] = order[C.UPDATED_AT[0]].split('T')[0]
            metadata[C.UPDATED_BY[0]] = order[C.UPDATED_BY[0]] or 'SYSTEM'

            order[C.METADATA] = metadata
            del order[C.PAYLOAD_DATA]
            order_list.append(order)
        return order_list

    except Exception:
        traceback.print_exc()
        return False