from apps.order_fulfiller.constants import Constant as C
from apps.order_fulfiller.services.db_service import create_order
from apps.order_fulfiller.services.client_service import get_client_id

def map_shopify_order_data(shopify_order_data):
    fi, si = C.INDEXES[C.FULFULLER], 1
    source = C.SHOPIFY
    client_id = get_client_id(shopify_order_data[C.APP_ID[si]])
    filtered_order_data = {
        C.ORDER_DETAILS: {
            C.ORDER_NO[fi]: str(shopify_order_data[C.ORDER_NO[si]]),
            C.APP_ID[fi]: str(shopify_order_data[C.APP_ID[si]]),
            C.PAYMENT_TYPE[fi]: shopify_order_data[C.PAYMENT_TYPE[si]],
            C.GROSS_AMOUNT[fi]: shopify_order_data[C.GROSS_AMOUNT[si]],
            C.CURRENCY[fi]: shopify_order_data[C.CURRENCY[si]],
            C.DISCOUNT[fi]: shopify_order_data[C.DISCOUNT[si]],
            C.TAX[fi]: shopify_order_data[C.TAX[si]],
            C.SOURCE_STATUS[fi]: shopify_order_data[C.SOURCE_STATUS[si]],
            C.SHIPPING_ADDRESS[fi]: shopify_order_data[C.SHIPPING_ADDRESS[si]],
            C.BILLING_ADDRESS[fi]: shopify_order_data[C.BILLING_ADDRESS[si]],
            C.CREATED_AT[fi]: shopify_order_data[C.CREATED_AT[si]],
            C.UPDATED_AT[fi]: shopify_order_data[C.UPDATED_AT[si]],
            C.SOURCE[fi]: C.SHOPIFY,
            C.SOURCE_TYPE[fi]: C.BRAND,
            C.SOURCE_WEBSITE[fi]: C.SOURCE_WEBSITE_URLS[source],
            C.STATUS[fi]: C.DEFAULT_ORDER_STATUS,
            C.CLIENT_ID[fi]: client_id
        },
        C.CUSTOMER_DETAILS: {
            C.CUSTOMER_EMAIL[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_EMAIL[si]],
            C.CUSTOMER_FIRST_NAME[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_FIRST_NAME[si]],
            C.CUSTOMER_LAST_NAME[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_LAST_NAME[si]],
            C.CUSTOMER_ORDER_COUNT[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_ORDER_COUNT[si]],
            C.CUSTOMER_STATE[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_STATE[si]],
            C.CUSTOMER_TOTAL_SPENT[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_TOTAL_SPENT[si]],
            C.CUSTOMER_LAST_ORDER_ID[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_LAST_ORDER_ID[si]],
            C.CUSTOMER_VERIFIED_EMAIL[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_VERIFIED_EMAIL[si]],
            C.CUSTOMER_TAX_EXEMPT[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_TAX_EXEMPT[si]],
            C.CUSTOMER_PHONE[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_PHONE[si]],
            C.CUSTOMER_CURRENCY[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_CURRENCY[si]],
            C.CUSTOMER_CREATED_AT[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_CREATED_AT[si]],
            C.CUSTOMER_UPDATED_AT[fi]: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_UPDATED_AT[si]],
        },
        C.DEFAULT_ADDRESS_DETAILS: shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_DEFAULT_ADDRESS[si]],
    }
    filtered_order_data[C.DEFAULT_ADDRESS_DETAILS][C.ZIP[fi]] = shopify_order_data[C.CUSTOMER[si]][C.CUSTOMER_DEFAULT_ADDRESS[si]][C.ZIP[si]]
    filtered_order_data[C.ORDER_DETAILS][C.SHIPPING_ADDRESS[fi]][C.ZIP[fi]] = shopify_order_data[C.SHIPPING_ADDRESS[si]][C.ZIP[si]]
    filtered_order_data[C.ORDER_DETAILS][C.BILLING_ADDRESS[fi]][C.ZIP[fi]] = shopify_order_data[C.BILLING_ADDRESS[si]][C.ZIP[si]]
    filtered_order_data[C.PAYLOAD_DATA] = shopify_order_data
    del filtered_order_data[C.DEFAULT_ADDRESS_DETAILS][C.ZIP[si]]
    del filtered_order_data[C.ORDER_DETAILS][C.SHIPPING_ADDRESS[fi]][C.ZIP[si]]
    del filtered_order_data[C.ORDER_DETAILS][C.BILLING_ADDRESS[fi]][C.ZIP[si]]
    return filtered_order_data


def create_shopify_order(shopify_order_data):
    filtered_data = map_shopify_order_data(shopify_order_data)
    res = create_order(filtered_data)
    return res