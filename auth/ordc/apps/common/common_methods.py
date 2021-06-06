from django.conf import settings
import string
import hashlib
import random
import time
from datetime import datetime
import uuid


from apps.common.logger import CustomLogger

logger = CustomLogger.get_logger(__name__)


def convert_to_dict(obj):
    """
    this will only object of dict and list or simple objects
    """
    if isinstance(obj, dict):
        result = {}
        for key, val in obj.items():
            if key.startswith("_"):
                continue
            else:
                result[key] = convert_to_dict(val)
        return result

    if isinstance(obj, list):  # if obj item is list of obj
        element = []
        for item in obj:
            element.append(convert_to_dict(item))
        return element

    if not hasattr(obj, "__dict__"):
        return obj

    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        else:
            result[key] = convert_to_dict(val)
    return result


def format_date(date):
    return date.strftime("%Y-%m-%d")


def convert_unix_time(date):
    if date:
        return time.mktime(date.timetuple())


def unix_to_native_date(unix_time):
    if unix_time:
        return datetime.utcfromtimestamp(int(unix_time))

    
