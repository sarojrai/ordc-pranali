from rest_framework.status import HTTP_400_BAD_REQUEST
import re


class ErrorObject(object):
    @classmethod
    def get_validation_error_init_obj(cls):
        return {
            "status": HTTP_400_BAD_REQUEST,
            "message": "Invalid request",
            "errors": [],
        }


class PrimitiveDataValidation(object):
    @classmethod
    def is_int(cls, value):
        try:
            num = int(value)
        except ValueError:
            return False
        return True


class FormFieldValidation(object):
    __phone_regex = "^[0-9]{10}$"
    __email_egex = "^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$"
    __name_regex = "[A-Za-z.]{2,25}( [A-Za-z]{2,25})?"

    @classmethod
    def is_valid_name(cls, name, allow_empty=True):
        if allow_empty:
            is_valid = re.fullmatch("[A-Za-z]{1,25}([A-Za-z. ]{2,25})?", name)
        else:
            is_valid = re.fullmatch("[A-Za-z]{1,25}([A-Za-z. ]{2,25})?", name)

        return bool(is_valid)

    @classmethod
    def is_valid_email(cls, email, allow_empty=True):
        if allow_empty:
            is_valid = re.fullmatch(
                "^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", email
            )
            return bool(is_valid)
        else:
            is_valid = re.fullmatch(
                "^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", email
            )
            return bool(is_valid)

    @classmethod
    def is_valid_phone(cls, phone, allow_empty=True):
        phone = str(phone)
        if allow_empty:
            is_valid = re.fullmatch("^[0-9]{10}$", phone)
            return bool(is_valid)
        else:
            is_valid = re.fullmatch("^[0-9]{10}$", phone)
            return bool(is_valid)

    @classmethod
    def is_valid_pincode(cls, pincode, allow_empty=False):
        pincode = str(pincode)
        if allow_empty:
            is_valid = re.fullmatch("^[0-9]{6}$", pincode)
            return bool(is_valid)
        else:
            is_valid = re.fullmatch("^[0-9]{6}$", pincode)
            return bool(is_valid)


class ValidationMessage(object):
    @classmethod
    def append_form_validation_error_msg(cls, value, response_error_obj, key):
        # return status and set validation  message
        if isinstance(response_error_obj, (list,)) and key:
            response_error_obj.append(
                {
                    "key": key,
                    "message": ("Enter valid {}" if value else "{} is required").format(
                        key
                    ),
                }
            )

    @classmethod
    def append_error_msg(cls, response_error_obj, key, error_message):
        response_error_obj.append({"key": key, "message": error_message})
