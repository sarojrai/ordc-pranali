from django.db import models
from django.utils.translation import ugettext_lazy as _

# from django_mysql.models import JSONField
from django.conf import settings
from django.contrib.auth import get_user_model


class CommonModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(null=True, auto_now=True, editable=False)
