from apps.notification.models import CommunicationMode, CommunicationEvent,\
                                     CommunicationChannel, ClientCommunication


class CommunicationManager:
    def __init__(self):
        pass

    def get_communication_modes(self, requested_data):
        is_success = True
        data = CommunicationMode.objects.all().values()
        return is_success, "message", list(data)
    
    def get_communication_channels(self, requested_data):
        is_success = True
        data = CommunicationChannel.objects.all().values()
        return is_success, 'message', list(data)
    
    def get_communication_events(self, requested_data):
        is_success = True
        data = CommunicationEvent.objects.all().values()
        return is_success, 'message', list(data)

    def get_client_communication(self, requested_data):
        is_success = True
        data = ClientCommunication.objects.all().values()
        return is_success, 'message', list(data)

    def create_client_communication(self, requested_data):
        is_success = True
        filter_data = {'channel_id': requested_data['channel_id'],
                       'client': requested_data['client_id'],
                       'sequence': requested_data['sequence']}
        
        del requested_data['client_id']
        del requested_data['channel_id']
        del requested_data['sequence']

        data = ClientCommunication.objects.get_or_create(**filter_data, defaults=requested_data)
        return is_success, 'message', list(data)