"""
Integrate APIs here

"""

#from httpclient import HTTPClient
from apps.common.httpclient import HTTPReq
import json

BASE_URL = "http://3.7.42.37:8080"


class CityAPI:
    def __init__(self):
        self.BASE_URL = BASE_URL
        self.PATH_URL = "/auth/api/cities/"
        self.query_string = "city_id={city_id}"
        self.http_client = HTTPReq(self.BASE_URL,self.PATH_URL)

    def get_city_name(self, city_id):
        #self.query_string = self.query_string.format(city_id=city_id)
        resp = self.http_client.http_get_call(self.query_string.format(city_id=city_id))
        return json.loads(resp.text)["data"][0]["name"]

class ServiceCenterAPI:
    def __init__(self):
        self.BASE_URL = BASE_URL
        self.PATH_URL = "/auth/api/sc/"
        self.query_string = "sc_id={sc_id}"
        self.http_client = HTTPReq(self.BASE_URL,self.PATH_URL)

    def get_sc_branch(self, sc_id):
        self.query_string = self.query_string.format(sc_id=sc_id)
        resp = self.http_client.http_get_call(self.query_string)
        return json.loads(resp.text)["data"][0]["name"]

class OrganisationAPI:
    def __init__(self):
        self.BASE_URL = BASE_URL
        self.PATH_URL = "/auth/api/organisations/"
        self.query_string = "org_id={org_id}"
        self.http_client = HTTPReq(self.BASE_URL,self.PATH_URL)

    def get_org_name(self, org_id):
        self.query_string = self.query_string.format(org_id=org_id)
        self.resp = self.http_client.http_get_call(self.query_string)
        return json.loads(self.resp.text)["data"][0]["name"]
