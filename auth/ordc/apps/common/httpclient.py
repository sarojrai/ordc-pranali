import threading
import json
import requests
from aenum import Enum

# logger import
from apps.common.logger import CustomLogger

logger = CustomLogger.get_logger(__name__)


class HttpMethod(Enum):
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"
    PUT = "PUT"

class HTTPReq:
    def __init__(self, base_url, path_url, headers=None):
        self.base_url = base_url
        self.path_url = path_url
        self.headers = headers
        self.url = self.base_url + self.path_url
    
    def http_get_call(self, query_string=None):
        logger.debug(f"http_get call start Url {self.url}{query_string}")
        url = self.url + query_string
        resp = requests.get(url, headers=self.headers)
        logger.debug(f"http_get call ends Url {self.url}{query_string}")
        return resp


class HTTPClient(object):
    def __init__(self, base_url, path_url, headers=None):
        self.base_url = base_url
        self.path_url = path_url
        self.headers = headers
        self.url = self.base_url + self.path_url

    def http_get(self, query_string=None):
        logger.debug(f"http_get call start Url {self.url}{query_string}")
        url = self.url + query_string
        resp = requests.get(url, headers=self.headers)
        logger.debug(f"http_get call ends Url {self.url}{query_string}")
        print("===================*************===================")
        print("---->", url, resp)
        return resp

    def http_post(self, data, query_string=None):
        logger.debug(f"http_post call start Url {self.url}{query_string} data={data}")
        url = self.url + query_string
        json_data = json.dumps(data)
        resp = requests.post(url, headers=self.headers, data=json_data)
        logger.debug(f"http_post call ends Url {self.url}{query_string}")
        return resp

    def http_put(self, data, query_string=None):
        logger.debug(f"http_put call start Url {self.url}{query_string} data={data}")
        url = self.url + query_string
        json_data = json.dumps(data)
        resp = requests.put(url, headers=self.headers, data=json_data)
        logger.debug(f"http_put call ends Url {self.url}{query_string}")
        return resp

    def http_delete(self, url, data, headers):
        pass

    def async_http_get(self, query_string=None):
        try:
            call_thread = threading.Thread(
                target=self.http_get, args=(query_string,), kwargs={}
            )
            call_thread.start()
            call_thread.is_alive()
        except Exception as ex:
            logger.error(f"error {ex} in calling async_http_get")

    def async_http_post(self, data, query_string=None):
        try:
            call_thread = threading.Thread(
                target=self.http_post,
                args=(
                    data,
                    query_string,
                ),
                kwargs={},
            )
            call_thread.start()
            call_thread.is_alive()
        except Exception as ex:
            logger.error(f"error {ex} in calling async_http_post")

    def async_http_put(self, data, query_string=None):
        try:
            call_thread = threading.Thread(
                target=self.http_put,
                args=(
                    data,
                    query_string,
                ),
                kwargs={},
            )
            call_thread.start()
            call_thread.is_alive()
        except Exception as ex:
            logger.error(f"error {ex} in calling async_http_put")
