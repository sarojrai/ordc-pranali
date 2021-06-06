from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'}, allow_null=False,
                                     allow_blank=False)
    invitation_token = serializers.CharField(
        allow_blank=False, allow_null=False)

class InvitationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    role_id = serializers.IntegerField(required=True)
    organisation_id = serializers.IntegerField(required=False)