from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .response import (
    ResponseEntity,
    ValidationErrorResponseEntity,
    ExceptionResponseEntity,
)


class APIViewInitializer(APIView):
    def __init__(self, **kwargs):
        super(APIViewInitializer, self).__init__(**kwargs)
        self.success_resp = ResponseEntity()
        self.exception_error_resp = ExceptionResponseEntity()
        self.validation_error_resp = ValidationErrorResponseEntity()
        self.errors = self.validation_error_resp.errors
        self.req_data = {}


class AuthenticatedAPIView(APIViewInitializer):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)


class AllowAnyAPIView(APIViewInitializer):
    permission_classes = (AllowAny,)
