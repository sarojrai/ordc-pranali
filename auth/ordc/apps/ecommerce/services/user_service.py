# -*- coding: utf-8 -*-
__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]


#Python Related dependencies
import logging
logger = logging.getLogger(__name__)
# Django related dependencies
from django.db.models import F

# Project Related dependencies
from apps.ecommerce.models import ProductCategory, SourceType, BrandWebsite,MarketPlace,CourierPartner,WarehouseManagement,CommunicationMode, ClientOnboarding
# from apps.common.common_methods import get_datetime_obj, format_date, get_datetime_str
class UserService():
    
    def product_category(self, requested_data):
        """ 
        Provide Product Category Details
        """
        resp = {}
        kwargs = {
            "status":1
        }
        code = requested_data.get('code','')
        if code !='':
            kwargs['code'] = code
        details = ProductCategory.objects.filter(**kwargs).values('id','code',label=F('description'))
        if details:
            data = []
            for detail in details:
                data.append(detail)
            resp["is_success"] = 'Success'
            resp["status_code"] = 200
            resp["message"] = 'You Fetched Product Category Details Successfully'
            resp["result"] = data
        else:
            resp["is_success"] =  'Failed'
            resp["status_code"] = 200
            resp["message"] = 'No Record Found'
            resp["result"] = {}
            
        logger.error(resp["message"])
        return resp

    def product_source(self, requested_data):
        """ 
        Provide P Source Type Details
        """
        resp = {}
        kwargs = {
            "status":1
        }
        code = requested_data.get('code','')
        if code !='':
            kwargs['code'] = code
        details = SourceType.objects.filter(**kwargs).values('id','code',label=F('description'))
        if details:
            data = []
            for detail in details:
                data.append(detail)
            resp["is_success"] = 'Success'
            resp["status_code"] = 200
            resp["message"] = 'You Fetched Source Type  Successfully'
            resp["result"] = data
        else:
            resp["is_success"] =  'Failed'
            resp["status_code"] = 200
            resp["message"] = 'No Record Found'
            resp["result"] = {}
            
        logger.error(resp["message"])
        return resp

