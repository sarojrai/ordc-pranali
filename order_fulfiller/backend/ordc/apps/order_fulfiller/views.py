import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from .constants import Constant as C
from .brand_website.shopify import create_shopify_order
from .services.db_service import get_all_orders
from .models import Order

class OrderView(APIView):

    def get(self, request):
        """
        Return all orders coming from different sources in the system.
        """
        try:
            res = get_all_orders()
            return Response({'status': 200, 'message': 'Success', 'data': res})            
        except Exception as e:
            traceback.print_exc()
            return Response({'status': 500, 'message': 'Error', 'data': {'error': str(e)}})

    def post(self, request, format=None):
        """
        Ingest all orders coming from different sources in the system.
        """
        try:
            res = {}
            brand_data = request.data
            if C.SHOPIFY in brand_data.get('order_status_url'):
                res = create_shopify_order(brand_data)
            return Response({'status': 200, 'message': 'Success', 'data': res})            
        except Exception as e:
            traceback.print_exc()
            return Response({'status': 500, 'message': 'Error', 'data': {'error': str(e)}})
