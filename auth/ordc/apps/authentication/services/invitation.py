import base64
from django.contrib.auth.models import User
from apps.authentication.models import EmployeeMaster
from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.authentication.models import UserInvitationToken, Organisation, Role
from ordc.settings import AUTH_PASSWORD_VALIDATORS

class InvitationService:

    def invite_user(self, email, organisation_id, role_id):
        UserDoesNotExist = False
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            UserDoesNotExist = True

        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            raise serializers.ValidationError("Role Does not exist")

        try:
            organisation = Organisation.objects.get(id=organisation_id)
        except Organisation.DoesNotExist:
            raise serializers.ValidationError("Organisation Does not exist")


        if UserDoesNotExist:
            # import ipdb; ipdb.set_trace()
            user = User.objects.create(email=email, username=email, is_active=False)
            EmployeeMaster.objects.create(email=email, status=0, user=user, employee_code=user.id, organisation=organisation, role=role)
            invitation_token = UserInvitationToken.objects.create(user=user)
            encoded = base64.urlsafe_b64encode(
                str(invitation_token.id).encode()).decode()
            print("Encoded ", encoded)
            return encoded
        else:
            raise serializers.ValidationError("User Already Exist")

    def complete_invitation(self, invitation_token, password):
        decoded_token = base64.urlsafe_b64decode(invitation_token.encode()).decode()
        invitation_token = get_object_or_404(UserInvitationToken, id=decoded_token)
        validate_password(password, user=invitation_token.user,
                          password_validators=get_password_validators(AUTH_PASSWORD_VALIDATORS))
        invitation_token.user.set_password(password)
        invitation_token.user.is_active = True
        invitation_token.user.save()
        UserInvitationToken.objects.filter(user=invitation_token.user).delete()


    def get_user_org(self, user):
        employee = get_object_or_404(EmployeeMaster, user=user)
        return employee.organisation.id