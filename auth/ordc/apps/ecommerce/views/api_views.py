# -*- coding: utf-8 -*-
__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]
#  Python module and packages
import json
import logging
LOGGER = logging.getLogger(__name__)
from datetime import datetime, timedelta

# # Django module and packages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

# # Project related module and packages
from apps.ecommerce.services.user_service import UserService
from apps.ecommerce.models import *




# Global Variable
STATUS = "status"
STATUS_CODE = "status_code"
MESSAGE = "message"
RESULT = "result"
SUCCESS = "Success"
FAILED = "Failed"



@api_view(["GET", "POST"])
@csrf_exempt
def product_category(request):
    """
    Returrn Product category list
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: ''
        }
    requested_data = {}
    if request.body:
        requested_data = json.loads(request.body)
    resp = UserService().product_category(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")

@api_view(["GET", "POST"])
@csrf_exempt
def product_source(request):
    """
    Returrn Source Type list
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    requested_data = {}
    if request.body:
        requested_data = json.loads(request.body)
    
    resp = UserService().product_source(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


