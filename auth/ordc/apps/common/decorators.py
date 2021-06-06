import functools
import timeit
from rest_framework import status

from common.logger import CustomLogger

logger = CustomLogger.get_logger(__name__)


def class_based_api_request_response_log(cls_method):
    @functools.wraps(cls_method)
    def wrapper(cls_obj, request, *args, **kwargs):
        start_time = timeit.default_timer()
        logger.info(
            f"Method: {cls_method.__name__} {cls_obj.__class__.__name__}  starts,\t"
            f"url : {request.path},\t"
            f"request body data {request.data} args {args} kwargs {kwargs},\t"
            f" query_params {request.query_params}"
        )
        response = cls_method(cls_obj, request, *args, **kwargs)

        status_code = response.status_code
        end_time = timeit.default_timer()
        if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            logger.exception(
                f"ApiError in Method: {cls_method.__name__} {cls_obj.__class__.__name__},\t"
                f"time {end_time - start_time},\t"
                f"starts url : {request.path},\t"
                f"status {status_code},\t"
                f"request body data {request.data} args {args} kwargs {kwargs},\t"
                f" query_params {request.query_params},\t "
                f"response data {response.data} "
            )
        elif status_code in (status.HTTP_400_BAD_REQUEST, status.HTTP_401_UNAUTHORIZED):
            logger.debug(
                f"ApiError Bad Request Method: {cls_method.__name__} {cls_obj.__class__.__name__},\t"
                f"time {end_time - start_time},\t"
                f"starts url : {request.path},\t"
                f"status {status_code},\t"
                f"request body data {request.data} args {args} kwargs {kwargs},\t"
                f" query_params {request.query_params},\t "
                f"response data {response.data} "
            )
        else:
            logger.debug(
                f"Completed Method: {cls_method.__name__} {cls_obj.__class__.__name__},\t"
                f"time {end_time - start_time},\t"
                f"starts url : {request.path},\t"
                f"status {status_code}"
            )

        return response

    return wrapper
