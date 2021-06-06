# # -*- coding: utf-8 -*-
# from apps.authentication.utils.common_utility import CommonUtility
# from apps.authentication.models import EmployeeMaster, EmployeeLoginHistory, UserOtp
# from apps.authentication.services.user_service import UserService
# from apps.authentication.serializers import InvitationSerializer, PasswordSerializer
# from apps.authentication.services.invitation import InvitationService
# from apps.authentication.services.email_service import EmailService
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
# from rest_framework import status
# from rest_framework import serializers
# from django.utils import timezone
# from django.db import transaction
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# from datetime import datetime, timedelta
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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets

# # Project related module and packages
from apps.authentication.services.user_service import UserService
from apps.authentication.models import EmployeeMaster, EmployeeLoginHistory, UserOtp
from apps.authentication.utils.common_utility import CommonUtility
from apps.authentication.services.location_service import LocationManager
from apps.common.restapiviewwrapper import ( Response, status, AuthenticatedAPIView, AllowAnyAPIView,)
from apps.common.response import ( ResponseEntity, ExceptionResponseEntity, ValidationErrorResponseEntity,)
from apps.common.common_methods import convert_to_dict
from apps.common.logger import CustomLogger


## Global Variables
LOGGER = CustomLogger.get_logger(__name__)

class Constant:
    IS_ERROR = True
    FAILED_STATUS = "FAILED"
    DEFUALT_MSG = "Something Went Wrong"
    POST = "POST"
    GET = "GET"
    ## TODO Move into constant

# Global Variable
STATUS = "status"
STATUS_CODE = "status_code"
MESSAGE = "message"
RESULT = "result"
DATA = "data"
SUCCESS = "Success"
FAILED = "Failed"
ISERROR = "is_error"


class CustomAuthToken(ObtainAuthToken):
    """ Fetching token
    """

    def post(self, request):
        """ post username for fetching token """

        response = {
            STATUS: FAILED,
            STATUS_CODE: 401,
            MESSAGE: "Invalid User",
            RESULT: {}}
        requested_data = json.loads(request.body)
        user_name = requested_data['username']
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            user = False
        if user:
            refresh = RefreshToken.for_user(user)
            response[STATUS] = 'Success'
            response[STATUS_CODE] = 200
            response[MESSAGE] = 'Token Fetched successfully'
            response[RESULT] = {'token': str(
                refresh.access_token), 'refresh': str(refresh)}
        response = json.dumps(response)
        return HttpResponse(response, content_type="application/json")


@api_view(["POST"])
@csrf_exempt
def user_registration(request):
    """
    Take user information as input for user registration and return result with status code
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    requested_data = json.loads(request.body)
    resp = UserService().user_register(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


@csrf_exempt
def login_user(request):
    """
    Take username and password as input and handles both authentication and authorization
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    requested_data = json.loads(request.body)
    user_name = requested_data.get('username')
    password = requested_data.get('password')
    if user_name == "" or password == "":
        response[STATUS] = FAILED
        response[STATUS_CODE] = 401
        response[MESSAGE] = 'Please enter username and password'
        response[RESULT] = {}
    else:
        user = authenticate(username=user_name, password=password)
        if user is not None:
            if user.is_active:
                # login is called
                # if requested_data.get('otp'):
                #     try:
                #         otp_details = UserOtp.objects.get(
                #             user_id=user.pk)
                #     except UserOtp.DoesNotExist:
                #         otp_details = None
                #     if otp_details is not None and otp_details.otp == requested_data.get('otp') and timezone.now() - otp_details.create_at < timedelta(minutes=15):
                #         del requested_data['otp']
                #     else:
                #         response[STATUS] = FAILED
                #         response[STATUS_CODE] = 200
                #         response[MESSAGE] = 'Invalid Otp'
                #         response[RESULT] = {}
                #         response = json.dumps(response)
                #         return HttpResponse(response, content_type="application/json")
                # else:
                #     random_otp = CommonUtility().random_with_n_digits(6)
                #     try:
                #         otp_details = UserOtp.objects.get(
                #             user_id=user.pk)
                #     except UserOtp.DoesNotExist:
                #         otp_details = None
                #     if otp_details is not None:
                #         otp_update_dict = {}
                #         otp_update_dict['otp'] = random_otp
                #         otp_update_dict['is_expired'] = 0
                #         otp_update_dict['create_at'] = datetime.now()
                #         otp_update = UserOtp.objects.filter(
                #             user_id=user.pk).update(**otp_update_dict)
                #     else:
                #         userotp = UserOtp()
                #         userotp.user_id = user.pk
                #         userotp.otp = random_otp
                #         userotp.save()
                #         # TODO OTP Need to be Sent to Mobile
                #     response[STATUS] = SUCCESS
                #     response[STATUS_CODE] = 200
                #     response[MESSAGE] = 'Check your Mobile for the OTP'
                #     response[RESULT] = {}
                #     response = json.dumps(response)
                #     return HttpResponse(response, content_type="application/json")
                emp_login_dict = {}
                del requested_data['username']
                del requested_data['password']
                try:
                    emp_details = EmployeeMaster.objects.get(
                        user_id=user.pk)
                except EmployeeMaster.DoesNotExist:
                    emp_details = False
                if emp_details:
                    emp_login_dict["employee_id"] = emp_details.id
                for key, value in requested_data.items():
                    emp_login_dict[key] = value
                try:
                    with transaction.atomic():
                        login(request, user)
                        login_details = EmployeeLoginHistory(
                            **emp_login_dict)
                        login_details.save()
                        # get refresh token
                        refresh = RefreshToken.for_user(user)
                        requested_data = {'token': str(refresh.access_token), 'refresh': str(refresh)}
                        response[STATUS] = SUCCESS
                        response[STATUS_CODE] = 200
                        response[MESSAGE] = 'You are successfully logged in'
                        response[RESULT] = requested_data
                except Exception as exp:
                    response[STATUS] = FAILED
                    response[STATUS_CODE] = 200
                    response[MESSAGE] = str(exp)
                    response[RESULT] = requested_data
            else:
                response[STATUS] = FAILED
                response[STATUS_CODE] = 401
                response[MESSAGE] = 'Your account is disabled'
                response[RESULT] = {}
        else:
            response[STATUS] = FAILED
            response[STATUS_CODE] = 401
            response[MESSAGE] = 'Invalid login credentials'
            response[RESULT] = {}
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    Logout from current session
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}

    try:
        # logout is called
        requested_data = json.loads(request.body)
        token = requested_data.get('refresh')
        refreshToken = RefreshToken(token)
        print(refreshToken)
        refreshToken.blacklist()
        logout(request)
        response[STATUS] = SUCCESS
        response[STATUS_CODE] = 200
        response[MESSAGE] = 'You have successfully logged out'
        response[RESULT] = {}
    except Exception as ex:
        print(ex)
        pass
    LOGGER.error(response[MESSAGE])
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


@api_view(["GET", "POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def user_detail(request):
    """
    Fetching users details
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    # TODO Allow Org Admin/SuperVisor or User Himself to Get Another/Own User Detail
    requested_data = json.loads(request.body)
    resp = UserService().user_detail(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)
    LOGGER.error(response[MESSAGE])
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_user_status(request):
    """
    Take empcode as input and change that empployee's status as active or in-active
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    # TODO Allow Only Super User or Org Admin to Change User Status
    requested_data = json.loads(request.body)
    resp = UserService().user_action(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


@csrf_exempt
@permission_classes([IsAuthenticated])
def update_profile(request):
    """
    Take inputs to be updated and send result with status code
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    # TODO Allow Only User to update it's profile information
    if request.POST or request.method == "POST":
        requested_data = json.loads(request.body)
        resp = UserService().update_profile(requested_data)
        if resp.get("is_success"):
            response[STATUS] = resp.get("is_success")
            response[STATUS_CODE] = resp.get(STATUS_CODE)
            response[MESSAGE] = resp.get(MESSAGE)
            response[RESULT] = resp.get(RESULT)
            response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def change_password(request):
    """
    Change password for user
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}
    requested_data = json.loads(request.body)
    resp = UserService().update_password(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)

    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")

def get_service_centre(request):
    mgr = LocationManager()
    response = {
            STATUS: 500,
            ISERROR: True,
            MESSAGE: "Something went wrong !!",
            DATA: []
        }

    is_success, data = mgr.get_service_centre()
    if is_success:
        response[STATUS] = 200
        response[ISERROR] = False
        response[DATA] = data
        response[MESSAGE] = "ServiceCentre(s) Details Fetched Successfully !"   

    return HttpResponse(json.dumps(response), content_type="application/json")

def get_cities(request):
    mgr = LocationManager()
    is_success, data = mgr.get_cities()
    response = {
            STATUS: 500,
            ISERROR: True,
            MESSAGE: "Something went wrong !!",
            DATA: []
        }

    if is_success:
        response[STATUS] = 200
        response[ISERROR] = False
        response[DATA] = data
        response[MESSAGE] = "City List Fetched Successfully !"

    return HttpResponse(json.dumps(response), content_type="application/json")

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def invite_user(request):
    try:
        response = {
            STATUS: FAILED,
            STATUS_CODE: 400,
            MESSAGE: "Something went wrong !!",
            RESULT: {}}
        serializer = InvitationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invitation_service = InvitationService()
        email = request.data['email']
        role_id = request.data['role_id']
        if 'organisation_id' in request.data:     
            org_id = request.data['organisation_id']
        elif request.user is not None:
            org_id = invitation_service.get_user_org(request.user)
        else:
            raise serializers.ValidationError('No Valid Organisation provided')
        token = invitation_service.invite_user(email, org_id, role_id)
        EmailService().invitation_email(email=email, token=token)
        response[STATUS_CODE] = 200
        response[MESSAGE] = "User Invited Successfully"
        response[STATUS] = 'SUCCESS'
        return HttpResponse(json.dumps(response))
    except serializers.ValidationError as e:
        response[STATUS_CODE] = 400
        response[MESSAGE] = str(e)
        return HttpResponse(
            json.dumps(response),
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        response[STATUS_CODE] = 500
        response[MESSAGE] = str(e)
        return HttpResponse(json.dumps(response), content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
def complete_invitation(request):
    try:
        response = {
            STATUS: FAILED,
            STATUS_CODE: 400,
            MESSAGE: "Something went wrong !!",
            RESULT: {}}
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invitation_token = request.data['invitation_token']
        password = request.data['password']
        InvitationService().complete_invitation(invitation_token, password)
        response[STATUS_CODE] = 200
        response[MESSAGE] = "User Registration Complete"
        response[STATUS] = 'SUCCESS'
        return HttpResponse(json.dumps(response))
    except serializers.ValidationError as e:
        response[STATUS_CODE] = 400
        response[MESSAGE] = str(e)
        return HttpResponse(
            json.dumps(response),
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        response[STATUS_CODE] = 500
        response[MESSAGE] = str(e)
        return HttpResponse(json.dumps(response), content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(["GET"])
@csrf_exempt
def get_organisation_groups(request):
    mgr = LocationManager()
    data = {}
    is_success, data['BrandWebsite'] = mgr.get_organisation(org_type=2)
    is_success, data['MarketPlace'] = mgr.get_organisation(org_type=3)
    is_success, data['WarehouseManagement'] = mgr.get_organisation(org_type=4)
    is_success, data['CourierPartner'] = mgr.get_organisation(org_type=5)
    response = {
            STATUS: 500,
            ISERROR: True,
            MESSAGE: "Something went wrong !!",
            DATA: []
        }
    if is_success:
        response[STATUS] = 200
        response[ISERROR] = False
        response[DATA] = data
        response[MESSAGE] = "Organisations Details Fetched Successfully !"
    
    return HttpResponse(json.dumps(response), content_type="application/json")

@api_view(["POST"])
@csrf_exempt
def client_onboarding(request):
    
    """
    Submit client - onboarding data 
    """
    response = {
        STATUS: FAILED,
        STATUS_CODE: 400,
        MESSAGE: "Something went wrong !!",
        RESULT: {}}

    requested_data = {}
    if request.body:
        requested_data = json.loads(request.body)
    resp = UserService().client_onboarding(requested_data)
    if resp.get("is_success"):
        response[STATUS] = resp.get("is_success")
        response[STATUS_CODE] = resp.get(STATUS_CODE)
        response[MESSAGE] = resp.get(MESSAGE)
        response[RESULT] = resp.get(RESULT)
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")

class OrganisationView(viewsets.ViewSet, AllowAnyAPIView):
    
    @action(detail=True, methods=[Constant.GET])
    def get_organisation(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = LocationManager().get_organisation(requested_data)
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