
class Constant:
    
    FULFULLER = "fulfuller"
    SHOPIFY = "shopify"
    AMAZON = "amazon"
    BRAND = "brand"
    MARKETING = "marketing"
    UNIQUE_ID = "unique_id"
    METADATA = "metadata"
    PAYLOAD_DATA = "payload_data"
    DEFAULT_ORDER_STATUS = "order_placed"
    ORDER_DETAILS = "order_details"
    CUSTOMER_DETAILS = "customer_details"
    DEFAULT_ADDRESS_DETAILS = "default_address_details"
    INDEXES = {FULFULLER: 0, SHOPIFY: 1, AMAZON: 2}
    SOURCE_WEBSITE_URLS = {SHOPIFY: 'https://www.shopify.in', AMAZON: 'https://www.amazon.in/'}
    # fulfiller, shopify, amazon
    # Order keys
    ORDER_NO = ("order_number", "order_number", "order_id")
    APP_ID = ("app_id", "app_id", "")
    PAYMENT_TYPE = ("payment_type", "gateway",)
    STATUS = ("status", "status",)
    GROSS_AMOUNT = ("gross_amount", "total_price",)
    CURRENCY = ("currency", "currency",)
    DISCOUNT = ("discount", "total_discounts",)
    TAX = ("tax", "total_tax",)
    SOURCE_STATUS = ("source_status", "financial_status",)
    BILLING_ADDRESS = ("billing_address", "billing_address",)
    SHIPPING_ADDRESS = ("shipping_address", "shipping_address",)
    CREATED_AT = ("created_at", "created_at",)
    UPDATED_AT = ("updated_at", "updated_at",)
    CUSTOMER = ("customer", "customer", "customer_details")
    CREATED_BY = ("created_by", "",)
    UPDATED_BY = ("updated_by", "",)
    IS_BLACKLISTED = ("is_blacklisted", "",)
    REQUESTED_PAYLOAD = ("requested_payload", "",)
    SOURCE_TYPE = ("source_type", "",)
    SOURCE = ("source", "",)
    SOURCE_WEBSITE = ("source_website", "",)
    CLIENT_ID = ("client_id", "",)

    # Customer Keys
    CUSTOMER_NAME = ("name", "name")    
    CUSTOMER_EMAIL = ("email", "email",)
    CUSTOMER_FIRST_NAME = ("first_name", "first_name",)
    CUSTOMER_LAST_NAME = ("last_name", "last_name",)    
    CUSTOMER_DEFAULT_ADDRESS = ("default_address", "default_address",)
    CUSTOMER_ORDER_COUNT = ("orders_count", "orders_count",)
    CUSTOMER_STATE = ("state", "state",)
    CUSTOMER_TOTAL_SPENT = ("total_spent", "total_spent",)
    CUSTOMER_LAST_ORDER_ID = ("last_order_id", "last_order_id",)
    CUSTOMER_VERIFIED_EMAIL = ("verified_email", "verified_email",)
    CUSTOMER_TAX_EXEMPT = ("tax_exempt", "tax_exempt",)
    CUSTOMER_PHONE = ("phone", "phone",)
    CUSTOMER_CURRENCY = ("currency", "currency",)
    CUSTOMER_CREATED_AT = ("created_at", "created_at",)
    CUSTOMER_UPDATED_AT = ("updated_at", "updated_at",)
    CUSTOMER_IS_BLACKLISTED = ("is_blacklisted", "")

    # Address Keys
    ADDRESS_1 = ("address1", "address1",)
    ADDRESS_2 = ("address2", "address2",)
    PHONE = ("phone", "phone",)
    CITY = ("city", "city",)
    ZIP = ("zipcode", "zip",)
    PROVINCE = ("province", "province",)
    COUNTRY = ("country", "country",)
    COMPANY = ("company", "company",)
    LATITUDE = ("latitude", "latitude",)
    LONGITUDE = ("longitude", "longitude",)
    COUNTRY_CODE = ("country_code", "country_code",)
    PROVINCE_CODE = ("province_code", "province_code",)
