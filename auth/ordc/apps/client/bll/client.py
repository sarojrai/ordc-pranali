# -*- coding: utf-8 -*-
__author__ = "Anil Kumar Gupta"
__copyright__ = "Copyright (©) 2018. ordc-warehouse-solution. All rights reserved."
__credits__ = ["ORDC"]

# python dependencies

# Django related dependencies

# Create your views here.
from apps.client.models import Client, ClientAddress, GST
from apps.authentication.utils.common_utility import CommonUtility
from apps.authentication.models import Country, State, City

class ClientManager():

    def get_clients(self, requested_data, **kwargs):
        clients = Client.objects.all().values()
        return True, "Message", list(clients)
    
    def create_client(self, requested_data, **kwargs):

        basic_data = requested_data['basic_detail']
        name = basic_data['name']
        client_type = basic_data['client_type']
        try:
            latest_id = Client.objects.letest('id')
        except:
            latest_id = 0
        code = CommonUtility().generate_code(client_type, latest_id)
        basic_data['code'] = code

        new_client = Client.objects.get_or_create(name=name, defaults=basic_data)
        message = 'New Client Added Successfully'
        return True, message, list(new_client)
    

    def customer_add_detail(self, customer_code, address_type=None): 
        """
        address_type string [BILLING, SHIPPING]
        """
        if not address_type:
            address_type='BILLING' #Default Add Type

        cust = Customer.objects.filter(code=customer_code)
        print("cust",cust, address_type)
        if cust:
            cust = cust.latest('id')
            try:
                if address_type=='BILLING':
                    return cust.billing_address()[0]
                elif address_type=='SIPPING':
                    return cust.shipping_address()[0]
                else:
                    return{}
            except:
                return{}
        else:
            return {} 
         
    def customer_update(self, detail):
        resp = {'message':"Something went wrong!!", 'status':1000, 'result':[]}
        name = detail['name']
        code = detail['code']
        website = detail['website']
        email = detail['email']
        contact_person = detail['contact_person']
        activated_by = detail['activated_by']
        activation_date = CommonUtility().get_datetime_now() 
        status = detail['status']
        customer_id = detail['customer_id']
        try:
            Customer.objects.filter(id=customer_id).update(name=name, code=code, website=website, \
                                    email=email, contact_person=contact_person,\
                                    activated_by_id=activated_by, activation_date=activation_date, status=status
                                    )
            resp['message'] = 'Client Updated Successfully'
            resp['status'] = 200
            resp['result'].append({'customer_id':str(customer_id)})
        except Exception as e:
            resp['messsage'] = str(e)
        return resp
    
    def same_as_billing_address(self, bill_id):
        """
        DOCString
        """
        resp = {'message':"Something went wrong!!", 'status':1000, 'result':[]}        
        cust_bill_add = CustomerAddress.objects.get(id=bill_id)
        if cust_bill_add.customer.customeraddress_set.filter(address_type_id=4):
            resp['message'] = 'Client Address already exist please update'
            return resp
        gst = cust_bill_add.gst_set.all()
        if gst:
            gst = gst.latest("id").id
        ##create new record in address model using billing add id
        cust_bill_add.pk = None
        cust_bill_add.address_type_id=4
        cust_bill_add.save()
        print("cust_bill_add",cust_bill_add.id)     
        
        ## create new gst record similar to billing for shipping address
        new_gst = GST.objects.get(id=gst)
        new_gst.pk = None
        new_gst.customer_address = cust_bill_add
        new_gst.save()
        print("new_gst.id",new_gst.id)     
        resp['message'] = 'Client Address Updated Successfully'
        resp['status'] = 200
        return resp
 
    def billing_address_update(self, detail):
        resp = {'message':"Something went wrong!!", 'status':1000, 'result':[]}
        address = detail['address']
        city = detail['city']
        state = detail['state']
        country = detail['country']
        pincode = detail['pincode']
        gst_number = detail['gst']
        contact = detail['contact']
        email = detail['email']
        mobile = detail['mobile']
        landmark = detail['landmark']
        customer_id = detail['customer_id']
        address_id = detail['address_id']
        address = address.split(" ")
        address1 = ' '.join(address[0:len(address)/3])
        address2 = ' '.join(address[len(address)/3:len(address)/3+len(address)/3])
        address3 = ' '.join(address[len(address)/3+len(address)/3:])
        address_type = detail['address_type'] ##3:Billing, 4:Shipping
        ##GST
        pan_number = gst_number[2:-3]
        state_gst_code = gst_number[:2]
        service_type = 1
        try:
            country = Country.objects.get(code=str(country).rstrip())
        except:
            country = Country.objects.get(code='IN') ##INDIA
        try:
            s = State.objects.get(country=country, code=str(state).rstrip())
        except Exception as e:
            print("E..", str(e))
        try:
            c=City.objects.get_or_create(state=s, code=str(city).rstrip(), name=str(city).rstrip())
        except Exception as e:
            print("E..1", str(e))
        try:
            try:
                existing_add = CustomerAddress.objects.filter(id=address_id)
            except:
                existing_add = None
            if existing_add:
                existing_add.update(customer_id=customer_id, address1=address1,\
                                                     address2=address2, address3=address3, \
                                                     city=c[0], state=s,\
                                                     pincode=pincode, contact_person=contact,\
                                                     email=email, mobile=mobile, landmark=landmark,\
                                                     address_type_id=address_type,
                                                    )
                new_add = existing_add[0]
            else:
                new_add = CustomerAddress.objects.get_or_create(customer_id=customer_id, address1=address1,\
                                                     address2=address2, address3=address3, \
                                                     city=c[0], state=s,\
                                                     pincode=pincode, contact_person=contact,\
                                                     email=email, mobile=mobile, landmark=landmark,\
                                                     address_type_id=address_type,
                                                    )
                new_add = new_add[0]
            gst = GST.objects.filter(customer_address = new_add)
            
            if gst:
                gst.update(customer_address=new_add, pan_number=pan_number, gst_number=gst_number, \
                       state_gst_code=state_gst_code,service_type_id=service_type)
            else:
                GST.objects.get_or_create(customer_address=new_add, pan_number=pan_number, gst_number=gst_number, \
                       state_gst_code=state_gst_code,service_type_id=service_type)

            resp['message'] = 'Client Address Updated Successfully'
            resp['status'] = 200
            resp['result'].append({'customer_id':str(customer_id)})
        except Exception as e:
            resp['messsage'] = str(e)
            print("E..", str(e))
        return resp

