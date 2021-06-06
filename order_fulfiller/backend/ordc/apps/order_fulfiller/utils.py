from .models import Order
from .serializer import OrderSerializer
from .constants import Constant as C

def map_request_data(brand_data, source):
    fi, si = C.INDEXES[C.FULFULLER], C.INDEXES[source]

    order_data = {
        C.CUSTOMER[fi]: {
            C.CUSTOMER_EMAIL[fi]: brand_data[C.CUSTOMER[si]][C.CUSTOMER_EMAIL[si]],
            C.CUSTOMER_FIRST_NAME[fi]: brand_data[C.CUSTOMER[si]][C.CUSTOMER_FIRST_NAME[si]],
            C.CUSTOMER_LAST_NAME[fi]: brand_data[C.CUSTOMER[si]][C.CUSTOMER_LAST_NAME[si]],
            C.CUSTOMER_DEFAULT_ADDRESS[fi]: brand_data[C.CUSTOMER[si]][C.CUSTOMER_DEFAULT_ADDRESS[si]],
        },
        C.ORDER_NO[fi]: brand_data[C.ORDER_NO[si]],
        C.PAYMENT_TYPE[fi]: brand_data[C.PAYMENT_TYPE[si]],
        C.GROSS_AMOUNT[fi]: brand_data[C.GROSS_AMOUNT[si]],
        C.CURRENCY[fi]: brand_data[C.CURRENCY[si]],
        C.DISCOUNT[fi]: brand_data[C.DISCOUNT[si]],
        C.TAX[fi]: brand_data[C.TAX[si]],
        C.SOURCE_STATUS[fi]: brand_data[C.SOURCE_STATUS[si]],
        C.SHIPPING_ADDRESS[fi]: brand_data[C.SHIPPING_ADDRESS[si]],
        C.BILLING_ADDRESS[fi]: brand_data[C.BILLING_ADDRESS[si]],
        C.CREATED_AT[fi]: brand_data[C.CREATED_AT[si]],
        C.UPDATED_AT[fi]: brand_data[C.UPDATED_AT[si]],
    }
    if (si == 1):
        order_data[C.SOURCE[fi]] = C.SHOPIFY
        order_data[C.SOURCE_TYPE[fi]] = C.BRAND
        order_data[C.SOURCE_WEBSITE[fi]] = C.SOURCE_WEBSITE_URLS[source]
        order_data[C.STATUS[fi]] = C.DEFAULT_ORDER_STATUS
        order_data[C.CLIENT_ID[fi]] = 'TEST'

    return order_data