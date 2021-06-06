# -*- coding: utf-8 -*-
__author__ = "Anil Kumar Gupta"
__copyright__ = "Copyright (©) 2018. ordc-warehouse-solution. All rights reserved."
__credits__ = ["ORDC"]

# python dependencies
import json
#from basicauth import decode

# Django related dependencies
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,RequestContext
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# from jsonview.decorators import *
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string, get_template
from django.apps import apps
from django.db.models import Count,Sum
from django.contrib.auth.decorators import login_required
get_model = apps.get_model


# Create your views here.
from apps.client.models import Client, CUST_TYPE
from apps.authentication.models import State
from apps.client.bll.client import ClientManager
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


# @csrf_exempt
# def customer(request):
#     customers = Customer.objects.filter()
#     return render(request,'wms_utility/masters/customer/customers.html', {"customers":customers})

@csrf_exempt
def customer_edit(request, pk):
    emp = request.user.employeemaster
    warehouse = emp.service_centre
    customer = Client.objects.get(id=pk)
    states = State.objects.all()
    if request.POST:
        response = {'message':"Invalid Request", 'status':1000, 'result':[]}
        ##Update Customer
        json_data = request.POST.get('detail')
        detail = json.loads(json_data)
        detail['activated_by'] = emp.id
        detail['customer_id'] = pk
        if detail["request_type"]=="DETAIL":
            resp = CustomerService().customer_update(detail)
            response = json.dumps(resp)
        elif detail["request_type"]=="BILLING_ADD":
            detail['address_type'] = 3
            resp = CustomerService().billing_address_update(detail)
            response = json.dumps(resp)
        elif detail["request_type"]=="SHIPPING_ADD":
            detail['address_type'] = 4
            resp = CustomerService().billing_address_update(detail)
            response = json.dumps(resp)
        else:        
            response = json.dumps(response)

        return HttpResponse(response, content_type="application/json")
    return render(request,'wms_utility/masters/customer/customer_edit.html', {"customer":customer, "states":states})



class ClientView(viewsets.ViewSet, AllowAnyAPIView):
    
    @action(detail=True, methods=[Constant.GET])
    def get_clients(self, request, *args, **kwargs):
        requested_data = json.loads(request.GET.get("params", '{}'))
        try:
            is_success, message, obj_details = ClientManager().get_clients(requested_data)
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
    def create_client(self, request, *args, **kwargs):
        requested_data = json.loads(request.body)
        try:
            is_success, message, obj_details = ClientManager().create_client(requested_data)
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


# @csrf_exempt
# def customer_create(request):
#     emp = request.user.employeemaster
#     warehouse = emp.service_centre
#     if request.POST:
#         response = {'message':"Invalid Request", 'status':1000, 'result':[]}
#         ##Create New Customer
#         json_data = request.POST.get('detail')
#         detail = json.loads(json_data)
#         print(detail)
#         detail['created_by'] = emp.id
#         resp = CustomerService().customer_create(detail)
#         resp_json = json.dumps(resp)
#         return HttpResponse(resp_json, content_type="application/json")
#     return render(request,'wms_utility/masters/customer/customer_create.html', {"customer_type":CUST_TYPE})


# @csrf_exempt
# def same_as_billing_add(request):
#     """
#     DOCString
#     """
#     if request.POST:
#         billing_address_id = request.POST['billing_address_id']
#         resp = CustomerService().same_as_billing_address(billing_address_id)
#         resp_json = json.dumps(resp)
#         return HttpResponse(resp_json, content_type="application/json")
     
# @csrf_exempt
# @json_view
# def city_detail(request):    
#     state=request.POST.get('state')
#     state=State.objects.get(id=state)
#     city=state.city_set.all()
#     cities={}
#     for c in city:
#         cities[c.id]=c.city_name
#     return cities


# @csrf_exempt
# @json_view
# def customer_add_detail(request):
#     customer_code = request.POST.get('customer_code')
#     address_type = request.POST.get('address_type')
#     resp = CustomerService().customer_add_detail(customer_code, address_type=address_type)
#     return resp

