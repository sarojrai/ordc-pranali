class ResponseUtils(object):
    def __init__(self):
        pass

    # Converts a simple object or list of simple objects into a python dict
    @staticmethod
    def convert_to_dict(obj):
        if isinstance(obj, dict):
            result = {}
            for key, val in obj.items():
                if key.startswith("_"):
                    continue
                else:
                    result[key] = ResponseUtils.convert_to_dict(val)
            return result

        if isinstance(obj, list):  # if obj item is list of obj
            element = []
            for item in obj:
                element.append(ResponseUtils.convert_to_dict(item))
            return element

        if not hasattr(obj, "__dict__"):
            return obj

        result = {}
        for key, val in obj.__dict__.items():
            if key.startswith("_"):
                continue
            else:
                result[key] = ResponseUtils.convert_to_dict(val)
        return result
