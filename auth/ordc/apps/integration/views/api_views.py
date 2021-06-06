__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]

#  Python module and packages
import json
import logging
LOGGER = logging.getLogger(__name__)

# # Django module and packages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

## Project related module and packages
from apps.common.restapiviewwrapper import ( Response, status, AuthenticatedAPIView, AllowAnyAPIView,)
from apps.common.response import ( ResponseEntity, ExceptionResponseEntity, ValidationErrorResponseEntity,)
from apps.common.common_methods import convert_to_dict
from apps.common.logger import CustomLogger
from apps.integration.bll.service import ServiceManager


## Global Variables
LOGGER = CustomLogger.get_logger(__name__)

class Constant:
    IS_ERROR = True
    FAILED_STATUS = "FAILED"
    DEFUALT_MSG = "Something Went Wrong"
    POST = "POST"
    GET = "GET"


class IntegrationView(viewsets.ViewSet, AllowAnyAPIView):
    
    @action(detail=True, methods=[Constant.GET])
    def get_service_type(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = ServiceManager().get_service_type(
                requested_data
            )
            if is_success:
                msg = message
                data = obj_details
            else:
                msg = message
                data = {}
            print(data)
            self.success_resp.message = msg
            self.success_resp.data = data
            self.success_resp.is_error = not is_success  ## Toggle the success msg
            return Response(
                status=status.HTTP_200_OK, data=convert_to_dict(self.success_resp)
            )
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=convert_to_dict(self.exception_error_resp),
            )

    @action(detail=True, methods=[Constant.GET])
    def get_service(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = ServiceManager().get_service(
                requested_data
            )
            if is_success:
                msg = message
                data = obj_details
            else:
                msg = message
                data = {}
            print(data)
            self.success_resp.message = msg
            self.success_resp.data = data
            self.success_resp.is_error = not is_success  ## Toggle the success msg
            return Response(
                status=status.HTTP_200_OK, data=convert_to_dict(self.success_resp)
            )
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=convert_to_dict(self.exception_error_resp),
            )
    
    @action(detail=True, methods=[Constant.POST])
    def create_service(self, request, *args, **kwargs):
        requested_data = json.loads(request.body)
        try:
            is_success, message, obj_details = ServiceManager().create_service(
                requested_data
            )
            if is_success:
                msg = message
                data = obj_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            self.success_resp.is_error = not is_success  ## Toggle the success msg
            return Response(
                status=status.HTTP_200_OK, data=convert_to_dict(self.success_resp)
            )
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=convert_to_dict(self.exception_error_resp),
            )