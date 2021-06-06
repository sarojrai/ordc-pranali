from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'}, required=True)
    invitation_token = serializers.CharField(required=True)


class InvitationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    role_id = serializers.IntegerField(required=True)
    organisation_id = serializers.IntegerField(required=False)
