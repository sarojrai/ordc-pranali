import requests
import traceback
from ordc.settings import config

def get_client_details():
    try:
        url = config('GET_CLIENT_DETAILS_URL')
        response = requests.get(url)
        data = response.json()
        return  data['data']
    except Exception as e:
        print('Error on calling GET_CLIENT_DETAILS API', str(e))
        traceback.print_exc()
        return None

def get_client_id(app_id):
    try:
        client_list = get_client_details()
        if client_list:
            for client in client_list:
                if str(app_id) == str(client.get('integration_identifier')):
                    return client['code']
        return None
    except Exception as e:
        print('Error getting client id', str(e))
        traceback.print_exc()
        return None
