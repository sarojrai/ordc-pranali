from apps.integration.models import ScmServiceType, ScmService


class ServiceManager:
    def __init__(self):
        pass

    def get_service_type(self, requested_data):
        is_success = True
        data = ScmServiceType.objects.all().values()
        return is_success, "message", list(data)

    def get_service(self, requested_data):
        is_success = True
        data = ScmService.objects.all().values()
        return is_success, "message", list(data)

    def create_service(self, requested_data):
        is_success = True
        filter_data = {'scm_type_id': requested_data['scm_type_id'],'client_id':requested_data['client_id']}
        del requested_data['scm_type_id']
        del requested_data['client_id']
        data = ScmService.objects.get_or_create(**filter_data, defaults=requested_data)
        return is_success, 'message', list(data)