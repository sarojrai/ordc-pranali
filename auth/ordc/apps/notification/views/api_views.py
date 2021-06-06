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
from apps.notification.bll.communication import CommunicationManager
from apps.notification.bll.ordc_email import EmailManager


## Global Variables
LOGGER = CustomLogger.get_logger(__name__)

class Constant:
    IS_ERROR = True
    FAILED_STATUS = "FAILED"
    DEFUALT_MSG = "Something Went Wrong"
    POST = "POST"
    GET = "GET"


class NotificationView(viewsets.ViewSet, AllowAnyAPIView):
    
    @action(detail=True, methods=[Constant.GET])
    def get_communication_modes(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = CommunicationManager().get_communication_modes(
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
    def get_communication_channels(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = CommunicationManager().get_communication_channels(
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
    
    @action(detail=True, methods=[Constant.GET])
    def get_communication_events(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = CommunicationManager().get_communication_events(
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
    
    @action(detail=True, methods=[Constant.GET])
    def get_client_communication(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = CommunicationManager().get_client_communication(
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
    
    @action(detail=True, methods=[Constant.POST])
    def create_client_communication(self, request, *args, **kwargs):
        requested_data = json.loads(request.body)
        try:
            is_success, message, obj_details = CommunicationManager().create_client_communication(
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
    
    @action(detail=True, methods=[Constant.GET])
    def notify(self, request, *args, **kwargs):
        requested_data = json.loads(request.body)
        try:
            is_success, message, obj_details = EmailManager().notify(
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