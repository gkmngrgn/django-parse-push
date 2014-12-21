from django.contrib import admin
from django.utils.text import Truncator
from django_parse_push.models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("truncated_device_id", "device_type", "user", "is_active", "created_at")

    def truncated_device_id(self, obj):
        return Truncator(obj.device_id).chars(50)


admin.site.register(Device, DeviceAdmin)
