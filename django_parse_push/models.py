from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_parse_push.utils import DeviceType

AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


@python_2_unicode_compatible
class Device(models.Model):
    user = models.ForeignKey(verbose_name=_("User"), to=AUTH_USER_MODEL, blank=True, null=True)
    device_type = models.CharField(verbose_name=_("Device Type"), max_length=50, choices=DeviceType.get_choices())
    device_id = models.TextField(verbose_name=_("Device ID"))
    is_active = models.BooleanField(verbose_name=_("Is device active?"), default=True,
                                    help_text=_("You can inactive devices will not be sent a notification"))
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Parse Device")
        verbose_name_plural = _("Parse Devices")
        ordering = ("-created_at",)
        unique_together = ("user", "device_type", "device_id")

    def __str__(self):
        return self.device_id
