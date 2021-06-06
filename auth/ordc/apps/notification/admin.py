from django.contrib import admin
from apps.notification.models import CommunicationMode, CommunicationEvent,\
                                     CommunicationChannel, ClientCommunication


class CommunicationModeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'priority','sequence', 'added_on', 'status')
    ordering = ('id',)

class CommunicationEventAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'notification_template', 'sequence', 'is_attachement', 'added_on', 'status')
    ordering = ('id',)
    
class CommunicationChannelAdmin(admin.ModelAdmin):
    list_display = ('mode','code', 'description', 'url', 'credentials','added_on', 'status')
    ordering = ('id',)

class ClientCommunicationAdmin(admin.ModelAdmin):
    list_display = ('channel','client', 'notification_template', 'priority','sequence','added_on', 'status')

admin.site.register(CommunicationMode, CommunicationModeAdmin)
admin.site.register(CommunicationEvent, CommunicationEventAdmin)
admin.site.register(CommunicationChannel, CommunicationChannelAdmin)
admin.site.register(ClientCommunication, ClientCommunicationAdmin)