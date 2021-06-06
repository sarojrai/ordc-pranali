from rest_framework import status
from typing import List


class DataEntity:
    def __init__(self):
        pass


class EmptyEntity:
    def __init__(self):
        pass


class ResponseBaseEntity(object):
    def __init__(self):
        self.is_error = False
        self.status = status.HTTP_200_OK
        self.message = "success"


class ResponseEntity(ResponseBaseEntity):
    def __init__(self):
        super().__init__()
        self.data = DataEntity()


class ValidationErrorResponseEntity(ResponseBaseEntity):
    def __init__(self):
        super().__init__()
        self.status = status.HTTP_400_BAD_REQUEST
        self.message = "Invalid request"
        self.is_error = True
        self.errors = []


class ExceptionResponseEntity(ResponseBaseEntity):
    def __init__(self):
        super().__init__()
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.message = " Some internal server error"
        self.is_error = True


class ErrorOutput:
    def __init__(self, key, message):
        self.key = key
        self.message = message


# Going forward all the apis should be written with the below response
class AbstractResponse(object):
    def __init__(self, hstatus=status.HTTP_200_OK, message=None, rtime=-1):
        self.status = hstatus
        self.message = message
        self.rtime = rtime


class ValidationErrorResponse(AbstractResponse):
    def __init__(
        self, hstatus=status.HTTP_500_INTERNAL_SERVER_ERROR, message=None, rtime=-1
    ):
        super().__init__(hstatus, message, rtime)
        self.errors: List[ErrorOutput] = []
